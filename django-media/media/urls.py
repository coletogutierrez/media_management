from django.contrib import admin
from django.urls import path, re_path, include

# from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


from . import views
from home import views as home_views


from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
router = routers.DefaultRouter()




router.register(r'artists', views.ArtistViewSet)
router.register(r'albums_with_filtering', views.AlbumViewSet, basename='albums_with_filtering')
router.register(r'albums_with_tracks', views.AlbumWithTracksViewSet)
router.register(r'tracks_with_filtering', views.TrackViewSet, basename='tracks_with_filtering')
router.register(r'albums_with_more_data', views.AlbumWithMoreDataViewSet, basename='albums_with_more_data')




from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [

    path('v1/', include(router.urls)),


    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]


