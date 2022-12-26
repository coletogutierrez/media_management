# -*- coding: utf-8 -*-

from rest_framework import serializers
from . models import *




class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'
        depth = 1


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        #fields = ('trackid', 'name', 'albumid', 'mediatypeid', 'genreid',
        #            'composer', 'milliseconds', 'bytes', 'unitprice')
        fields = ('name', 'composer', 'milliseconds', 'bytes', 'unitprice', 'albumid')
        depth = 1

class AlbumWithTracksSerializer(serializers.HyperlinkedModelSerializer):

    own_tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('albumid', 'title', 'artistid', 'own_tracks')
        depth = 1

class AlbumWithMoreDataSerializer(serializers.HyperlinkedModelSerializer):

    get_total_tracks = serializers.IntegerField()

    class Meta:
        model = Album
        fields = ('albumid', 'title', 'artistid', 'get_total_tracks')
        depth = 1










