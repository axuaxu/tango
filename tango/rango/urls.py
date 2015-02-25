from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),  # New!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'), # NEW MAPPING!
    url(r'^about', views.about, name='about'),
    url('', views.index, name='index'),

)
