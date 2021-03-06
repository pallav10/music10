from django.conf.urls import url
import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^genre/$', views.GenreCreate.as_view(), name='genre-add'),
    url(r'^genres/$', views.get_all_genres),
    url(r'^genres/(?P<pk>[0-9]+)/$', views.genre_detail),
    url(r'^track/$', views.SongCreate.as_view(), name='song-add'),
    url(r'^tracks/$', views.get_all_tracks, name='tracks'),
    url(r'^tracks/(?P<pk>[0-9]+)/$', views.track_detail),
    url(r'^delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
]
