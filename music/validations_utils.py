from rest_framework import status

import exceptions_utils
import messages
from models import Song, Genre


def track_validation(key):
    try:
        track = Song.objects.get(pk=key)
        return track
    except Song.DoesNotExist:
        raise exceptions_utils.ValidationException(messages.SONG_DOES_NOT_EXISTS, status.HTTP_404_NOT_FOUND)


def genre_validation(key):
    try:
        genre = Genre.objects.get(pk=key)
        return genre
    except Genre.DoesNotExist:
        raise exceptions_utils.ValidationException(messages.GENRE_DOES_NOT_EXISTS, status.HTTP_404_NOT_FOUND)
