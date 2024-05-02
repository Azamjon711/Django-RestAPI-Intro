from django.urls import path, include
from .views import ArtistAPIView, AlbumAPIView, ArtistDetailAPIView, AlbumDetailAPIView
from .views import SongAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("song", viewset=SongAPIViewSet)


urlpatterns = [
    path("artist/", ArtistAPIView.as_view(), name="artist"),
    path("artist/<int:id>/", ArtistDetailAPIView.as_view(), name="artist-detail"),
    path("album/", AlbumAPIView.as_view(), name="album"),
    path("album/<int:id>/", AlbumDetailAPIView.as_view(), name="album-detail"),
    # path("song/", SongAPIView.as_view(), name="song"),
    path("", include(router.urls)),
]
