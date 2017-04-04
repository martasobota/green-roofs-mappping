"""Green_Roof_MapPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from warsaw.views import AddGreenRoofView, DeleteGreenRoofView, LoginView, LogoutView, UpdateGreenRoofView, WarsawView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WarsawView.as_view(), name='index')
    url(r'^add_green_roof', AddGreenRoofView.as_view(), name='add-green-roof'),
    url(r'^update_subject/(?P<pk>(\d)+)', UpdateGreenRoofView.as_view(), name='update-green-roof'),
    url(r'^delete_green_roof/(?P<pk>(\d)+)', DeleteGreenRoofView.as_view(), name='delete-green-roof'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'), #do name odwołujemy się w reversie
]
