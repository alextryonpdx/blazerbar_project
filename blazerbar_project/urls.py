from django.conf.urls import patterns, include, url
from django.contrib import admin
from blazerbar import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blazerbar_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^blazerbar/games/$', views.get_games, name='get_games'),
    url(r'^/about/$', views.about, name="about"),
    url(r'^blazerbar/bars/$', views.get_bars, name='get_bars'),
    url(r'^blazerbar/teams/$', views.teams, name='teams'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/$', views.bar_page, name='bar_page'),
    url(r'^blazerbar/(?P<team_id>[\w\-]+)/$', views.get_games, name='get_games'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')

   # url(r'^blazerbar/friends/', views.get_friends, name='get_friends')
    )


 #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )