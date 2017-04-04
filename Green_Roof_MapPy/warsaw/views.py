from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import AuthForm, SearchForm
from warsaw.models import GreenRoof, District, City

# Create your views here.
class WarsawView(View):
	def get(self, request):
		return render(request, 'warsaw/base.html')
		greenroofs = GreenRoof.objects.order_by('roof_address')
		template = loader.get_template('warsaw/base.html')
		context = RequestContext(request, {
        'greenroofs': greenroofs, 'content': render_to_string('warsaw/base.html', {'waypoints': waypoints})
    })
		return HttpResponse(template.render(context))

class LoginView(View):
	def get(self, request):
		form = AuthForm()
		ctx = {'form' : form}
		return render(request, 'warsaw/login.html', ctx) 

	def post(self, request):
		form = AuthForm(data=request.POST)
		ctx = {'form' : form}
		if form.is_valid():
			user = form.cleaned_data['user']
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'warsaw/login.html', ctx)		

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('index'))

	def detail(request, poll_id):
		p = get_object_or_404(Poll, pk=poll_id)
		return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

class AddGreenRoofView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = ['warsaw.add_greenroof']
	raise_exception = True
	model = GreenRoof #zaimportować klasę
	fields = '__all__' #nie ma kwadratowych nawiasów, bo nie tworzymy listy, tylko bierzemy ALL

	def handle_no_permission(self):
		if not self.request.user.is_authenticated:
			return HttpResponseRedirect(reverse('login'))
		else:
			return super().handle_no_permission()


class GreenRoofSearchView(View):
	def get(self, request):
		ctx = {'form' : SearchForm()}
		return render(request, 'student_search.html', ctx)

	def post(self, request):
		form = SearchForm(data=request.POST)
		ctx = {'form' : form}
		if form.is_valid():
			address = form.cleaned_data['address']
			greenroofs = GreenRoof.objects.filter(roof_address__icontains=address)
			ctx['results'] = greenroofs
		return render(request, 'gr_results.html', ctx)

class UpdateGreenRoofView(UpdateView):
	model = GreenRoof
	fields = '__all__'

class DeleteGreenRoofView(DeleteView):
	model = GreenRoof
	success_url = reverse_lazy('index')

