from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *


from rest_framework import generics
from rest_framework.pagination import CursorPagination

class Pagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100




class YoutubeVideos(generics.ListAPIView):#list view for showing JSON response
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    filterset_fields = ['channel_id','channel_title']
  
    ordering = ('-publishedDateTime')
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    pagination_class = Pagination