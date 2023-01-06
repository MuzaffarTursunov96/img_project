from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserImageListSerializer, UserImageNameSerializer, UserImagePostSerializer, UserImageDetailSerializer
from .models import UserImage

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


class UserImageApi(generics.CreateAPIView):
    queryset = UserImage.objects.all()
    permission_classes = (IsAuthenticated, )
    parser_classes = [MultiPartParser, ]
    serializer_class = UserImagePostSerializer

    def post(self, request):
        serializer = UserImagePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserImageListApi(generics.ListAPIView):
    queryset = UserImage.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserImagePostSerializer
    

    def get(self, request, format=None):
        if 'sort' in request.GET:
            sort = request.GET.get('sort', None)
            if sort == "asc":
                images = UserImage.objects.all().order_by('created_date')
            elif sort == "desc":
                images = UserImage.objects.all().order_by('-created_date')
            elif sort == 'geo':
                images = UserImage.objects.all().order_by('meta_geolocation')
            elif sort == 'name':
                images = UserImage.objects.all().order_by('meta_name')
            else:
                images = UserImage.objects.all()
        else:
            images = UserImage.objects.all()

        serializer = UserImageListSerializer(images, many=True)
        return Response(serializer.data)


class UserImageDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    def get_object(self, pk):
        try:
            return UserImage.objects.get(pk=pk)
        except UserImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        img = self.get_object(pk)
        serializer = UserImageDetailSerializer(img)
        return Response(serializer.data)


class ImageDelete(generics.DestroyAPIView):
    queryset = UserImage.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserImagePostSerializer
    lookup_url_kwarg = 'pk'


class UserImageFilterByName(generics.ListAPIView):
  queryset =UserImage.objects.all()
  serializer_class =UserImageNameSerializer
  lookup_url_kwarg ='name'
  permission_classes = (IsAuthenticated, )

  def get(self, request, name):
    img=UserImage.objects.filter(meta_name__icontains=name)
    serializer = UserImageNameSerializer(img,many=True)
    return Response(serializer.data)
