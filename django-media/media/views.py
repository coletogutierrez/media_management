from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import get_object_or_404
from django.db.models import Q
#from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django.db.models import Count

from django.shortcuts import render

from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect


from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request




        
import random



# import json
# from django.http import JsonResponse

from . models import *
#from rest_framework.pagination import PageNumberPagination
from . serializers import *
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
BASE_DIR = getattr(settings, "BASE_DIR", None)






class QueryParamAuthentication(TokenAuthentication):
    query_param_name = 'token'

    def authenticate(self, request):
        token = request.query_params.get(self.query_param_name)
        if token:
            return self.authenticate_credentials(token)
        return None




class AlbumViewSet(viewsets.ModelViewSet):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)

    serializer_class = AlbumSerializer

    authentication_classes = (TokenAuthentication, QueryParamAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):

        artist_id = self.request.query_params.get('artist', None)
        
        if artist_id:
            queryset = Album.objects.using('chinook').filter(artistid=artist_id)
        else:   
            queryset = Album.objects.using('chinook').all()

        return queryset


class ArtistViewSet(viewsets.ModelViewSet):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)

    queryset = Artist.objects.using('chinook').all()
    serializer_class = ArtistSerializer

    authentication_classes = (TokenAuthentication, QueryParamAuthentication,)
    permission_classes = (IsAuthenticated,)


class AlbumWithTracksViewSet(viewsets.ModelViewSet):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)

    queryset = Album.objects.using('chinook').prefetch_related('own_tracks').all()
    serializer_class = AlbumWithTracksSerializer

    authentication_classes = (TokenAuthentication, QueryParamAuthentication,)
    permission_classes = (IsAuthenticated,)


class TrackViewSet(viewsets.ModelViewSet):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)

    serializer_class = TrackSerializer

    authentication_classes = (TokenAuthentication, QueryParamAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        album_id = self.request.query_params.get('album', None)
        
        if album_id:
            queryset = Track.objects.using('chinook').filter(albumid=album_id)
        else:   
            queryset = Track.objects.using('chinook').all()

        return queryset


class AlbumWithMoreDataViewSet(viewsets.ModelViewSet):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)

    serializer_class = AlbumWithMoreDataSerializer

    authentication_classes = (TokenAuthentication, QueryParamAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        queryset = Album.objects.using('chinook').select_related('artistid').all().annotate(get_total_tracks=Count('own_tracks'))

        return queryset









