"""stratinum URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from imagec import views as imagec_views
from contact import views as contact_views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', imagec_views.home, name='home'),
    url(r'^signup1/$', imagec_views.signup1, name='signup1'),
    url(r'^profile/$', imagec_views.userProfile, name='profile'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^post/$', imagec_views.post_detail, name='post_detail'),
    url(r'^post/new/$', imagec_views.post_new, name='post_new'),
    url(r'^post/edit/$', imagec_views.post_edit, name='post_edit'),
    url(r'^accounts/', include('allauth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^newhome/$', imagec_views.newhome, name='newhome'),
    url(r'^create_form/$', imagec_views.create_form, name='create_form'),
    url(r'^profile/edit/$', imagec_views.edit_profile, name='edit_profile'),
    url(r'^about/$', imagec_views.about, name='about'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

