from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import utils
import validations_utils
from exceptions_utils import ValidationException
from models import Genre, Song
from serializers import GenreSerializer, SongSerializer
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.


@api_view(['POST'])
@cache_page(60 * 15)
def genre(request):
    if request.method == 'POST':
        try:
            data = request.data
            genre_data = utils.create_genre(data)  # Creates genre with request data.
            return Response(genre_data, status=status.HTTP_201_CREATED)
        except ValidationException as e:  # Generic exception
            return Response(e.errors, status=e.status)


@api_view(['POST'])
@cache_page(60 * 15)
def song(request):
    if request.method == 'POST':
        try:
            data = request.data
            song_data = utils.create_song(data)  # Creates song with request data.
            return Response(song_data, status=status.HTTP_201_CREATED)
        except ValidationException as e:  # Generic exception
            return Response(e.errors, status=e.status)


@api_view(['GET'])
@cache_page(60 * 15)
def get_all_genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        genre_serializer = GenreSerializer(genres, many=True)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@cache_page(60 * 15)
def genre_detail(request, pk):
    data = request.data
    try:
        genre_info = validations_utils.genre_validation(pk)
    except ValidationException as e:  # Generic exception
        return Response(e.errors, status=e.status)

    if request.method == 'GET':
        genre_serializer = GenreSerializer(genre_info)
        return Response(genre_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            updated_genre = utils.update_genre(data, genre_info)  # Updates genre details.
            return Response(updated_genre, status=status.HTTP_200_OK)
        except ValidationException as e:  # Generic exception
            return Response(e.errors, status=e.status)


@api_view(['GET'])
@cache_page(60 * 15)
def get_all_tracks(request):
    query_params = request.query_params.dict()  # Gets parameters.
    if request.method == 'GET':
        if 'song_title' in query_params:
            filter_by_title = str(query_params['song_title'][:-1] if '/' in query_params['song_title']
                                  else query_params['song_title'])
            track = Song.objects.filter(song_title=filter_by_title)  # Get all tracks for particular title
            track_serializer = SongSerializer(track, many=True)
            return Response(track_serializer.data, status=status.HTTP_200_OK)
        elif 'genre' in query_params:
            filter_by_genre = str(query_params['genre'][:-1] if '/' in query_params['genre']
                                  else query_params['genre'])
            track = Song.objects.filter(genre=filter_by_genre)  # Get all tracks for particular genre
            track_serializer = SongSerializer(track, many=True)
            return Response(track_serializer.data, status=status.HTTP_200_OK)
        else:
            track = Song.objects.all()  # Get all tracks
            track_serializer = SongSerializer(track, many=True)
            return Response(track_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@cache_page(60 * 15)
def track_detail(request, pk):
    data = request.data
    try:
        track = validations_utils.track_validation(pk)
    except ValidationException as e:  # Generic exception
        return Response(e.errors, status=e.status)

    if request.method == 'GET':
        track_serializer = SongSerializer(track)
        return Response(track_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            updated_track = utils.update_track(data, track)  # Updates track details.
            return Response(updated_track, status=status.HTTP_200_OK)
        except ValidationException as e:  # Generic exception
            return Response(e.errors, status=e.status)


def index(request):
    tracks = Song.objects.all()  # Get all tracks
    track_serializer = SongSerializer(tracks, many=True)
    track_data = track_serializer.data
    genres = Genre.objects.all()  # get all genres.
    genre_serializer = GenreSerializer(genres, many=True)
    genre_data = genre_serializer.data
    context = {'tracks': track_data,
               'genres': genre_data,
               }
    return render(request, 'music/index.html', context)


class SongCreate(CreateView):
    model = Song
    fields = ['song_title', 'genre']


class GenreCreate(CreateView):
    model = Genre
    fields = ['genre']
