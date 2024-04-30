from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={'getAPI': 'GET Landing Page API view'})

    def post(self, request):
        return Response(data={'postAPI': ' POST Landing Page API view'})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists, many=True)
        return Response(data=serializers.data)


class AlbumAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializers = AlbumSerializer(albums, many=True)
        return Response(data=serializers.data)


class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializers = SongSerializer(songs, many=True)
        return Response(data=serializers.data)


