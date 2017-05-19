from rest_framework import serializers
from models import Song, Genre


# it holds the value of song table with all fields.
class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'song_title', 'genre', 'audio_file', 'ratings', 'is_deleted')


# it holds the value of genre table with all fields.
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'genre', 'is_favorite', 'is_deleted')
