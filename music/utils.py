from rest_framework import status

import exceptions_utils
from serializers import GenreSerializer, SongSerializer


def create_genre(data):
    genre_serializer = GenreSerializer(data=data)
    if genre_serializer.is_valid():
        genre = genre_serializer.save()
        keys = ['id', 'genre', 'is_favorite']  # data that we want to return as JSON response
        response = {k: v for k, v in genre_serializer.data.iteritems() if k in keys}
        return response
    else:
        raise exceptions_utils.ValidationException(genre_serializer.errors, status.HTTP_400_BAD_REQUEST)


def create_song(data):
    song_serializer = SongSerializer(data=data)
    if song_serializer.is_valid():
        song = song_serializer.save()
        keys = ['id', 'song_title', 'genre', 'audio_file', 'ratings']  # data that we want to return as JSON response
        response = {k: v for k, v in song_serializer.data.iteritems() if k in keys}
        return response
    else:
        raise exceptions_utils.ValidationException(song_serializer.errors, status.HTTP_400_BAD_REQUEST)


def update_track(data, track):
    track_serializer = SongSerializer(data=data, instance=track)
    if track_serializer.is_valid():
        track_serializer.save()
        return track_serializer.data
    else:
        raise exceptions_utils.ValidationException(track_serializer.errors, status.HTTP_400_BAD_REQUEST)


def update_genre(data, genre_info):
    genre_serializer = GenreSerializer(data=data, instance=genre_info)
    if genre_serializer.is_valid():
        genre_serializer.save()
        return genre_serializer.data
    else:
        raise exceptions_utils.ValidationException(genre_serializer.errors, status.HTTP_400_BAD_REQUEST)
