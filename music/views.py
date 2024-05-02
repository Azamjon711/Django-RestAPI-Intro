from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


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


# class SongAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         serializers = SongSerializer(songs, many=True)
#         return Response(data=serializers.data)


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumDetailAPIView(APIView):
    def get(self, request, id):
        try:
            album = Album.objects.get(id=id)
            serializer = AlbumSerializer(album)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=album, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        album = Album.objects.get(id=id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
