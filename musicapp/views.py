
from django.http import JsonResponse, HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets

class ArtistApiView(APIView):
    serializer_class = ArtistSerializer
    def get(self, request):
        allArtists = Artist.objects.all().values()
        return Response({'Message':'List of Artists', 'Artist List':allArtists})

    def post(self, request):
        print('Request data is: ',request.data)
        serializer_obj= ArtistSerializer(data=request.data)
        if (serializer_obj.is_valid()):
            Artist.objects.create(first_name=serializer_obj.data.get('first_name'),
                                  last_name=serializer_obj.data.get('last_name'),
                                  age=serializer_obj.data.get('age')
        )
        artist=Artist.objects.all().filter(first_name=request.data['first_name']).values()
        return Response({'Message': 'New Artist added', 'Artiste': artist})

class SongViewSet(viewsets.ModelViewSet):
    queryset =Song.objects.all()
    serializer_class = SongSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset =Lyric.objects.all()
    serializer_class = LyricSerializer











"""  

class SongApiView(APIView):
    serializer_class = SongSerializer
    def get(self, request):
        allSongs = Song.objects.all().values()
        allLyricss = Lyric.objects.all().values()
        return Response({'Message':'List of Songs', 'Song List':allSongs}),
        return Response({'Message':'List of Lyrics', 'Song List':allLyrics})

    def post(self, request):
        print('Request data is: ',request.data)
        serializer_obj= SongSerializer(data=request.data)
        serializer_obj= LyricSerializer(data=request.data)
        if (serializer_obj.is_valid()):
            Song.objects.create(title= serializer_obj.data.get('title'),
                                date_released= serializer_obj.data.get('dates_released'),
                                likes= serializer_obj.data.get('likes'),
                                artiste_id= serializer_obj.data.get('artiste_id')
                                )
        song =Song.objects.all().filter(song_title=request.data['song_title']).values()
        return Response({'Message': 'New Lyric added', 'Lyrics': song})

class LyricApiView(APIView):
    serializer_class = LyricSerializer
    def get(self, request):
        allLyrics = Lyric.objects.all().values()
        return Response({'Message':'List of Lyrics', 'Song List':allLyrics})

    def post(self, request):
        print('Request data is: ',request.data)
        serializer_obj= LyricSerializer(data=request.data)
        if (serializer_obj.is_valid()):
            Lyric.objects.create(song_title= serializer_obj.data.get('song_title'),
                                 content= serializer_obj.data.get('content'),
                                 song_id= serializer_obj.data.get('song_id'),
            )
        lyric =Lyric.objects.all().filter(song_title=request.data['song_title']).values()
        return Response({'Message': 'New Lyric added', 'Lyrics': lyric})
"""  


