"""BBSSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bbs/', views.top_ten, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^top_ten/', views.top_ten, name='top_ten'),
    url(r'^to_post/', views.to_post, name='to_post'),
    url(r'^post/', views.post, name='post'),
    url(r'^stick_post/', views.stick_post, name='stick_post'),
    url(r'^reply/', views.reply, name='reply'),
    url(r'^notification/', views.notification, name='reply'),
]
