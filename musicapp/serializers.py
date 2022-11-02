from .models import Artist, Song, Lyric
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields =('__all__')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =('__all__')

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields =('__all__')
        
