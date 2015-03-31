from django.conf.urls import patterns, include, url
from django.contrib import admin
from blazerbar import views
from django.conf import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blazerbar/games/$', views.get_games, name='get_games'),
    url(r'^/about/$', views.about, name="about"),
    url(r'^blazerbar/bars/$', views.get_bars, name='get_bars'),
    url(r'^blazerbar/teams/$', views.teams, name='teams'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/$', views.bar_page, name='bar_page'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/watch-here/(?P<username>[\w\-]+)/$', views.watch_here, name='watch_here'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/watch-here/(?P<username>[\w\-]+)/g/(?P<game_id>[\w\-]+)$', views.event_from_bar, name='event_from_bar'),
    url(r'^blazerbar/bar/(?P<game_id>[\w\-]+)/watch-this/(?P<username>[\w\-]+)/$', views.watch_here, name='watch_this'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/(?P<username>[\w\-]+)/review/$', views.review_bar, name='review_bar'),
    url(r'^blazerbar/bar/(?P<bar_slug>[\w\-]+)/(?P<username>[\w\-]+)/favorite/$', views.favorite, name='favorite'),
    #url(r'^blazerbar/team/(?P<team_id>[\w\-]+)/$', views.get_games, name='get_games'),
    url(r'^blazerbar/game/(?P<game_id>[\w\-]+)/$', views.game, name='game'),
    url(r'^blazerbar/register/', views.register, name='register'),
    url(r'^blazerbar/join-event/(?P<eventID>[\w\-]+)$', views.join_event, name='join_event'),
    url(r'^blazerbar/leave-event/(?P<eventID>[\w\-]+)$', views.leave_event, name='leave_event'),
    url(r'^blazerbar/event/(?P<eventID>[\w\-]+)$', views.event, name='event'),
    url(r'^blazerbar/friend/(?P<username>[\w\-]+)$', views.add_friend, name='add_friend'),
    url(r'^blazerbar/unfriend/(?P<username>[\w\-]+)$', views.remove_friend, name='remove_friend'),
    url(r'^blazerbar/team/(?P<team_id>[\w\-]+)/$', views.team_page, name='team_page'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^barsearch/$', views.find_bars, name='get_bars'),
    url(r'^blazerbar/userprofile/(?P<username>[\w\-]+)/$', views.user_profile, name='userpage'),
    url(r'^blazerbar/deny/(?P<eventID>[\w\-]+)$', views.deny_invite, name='deny_invite'),
    url(r'^blazerbar/accept/(?P<eventID>[\w\-]+)$', views.accept_invite, name='accept_invite'),
    url(r'^blazerbar/editprofile/(?P<username>[\w\-]+)/$', views.editprofile, name='edit_profile'),
)



 #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )