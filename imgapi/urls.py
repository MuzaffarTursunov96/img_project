
from django.urls import path
from . import views




urlpatterns = [
    path('image-add', views.UserImageApi.as_view(), name='image_add'),
    path('image-list', views.UserImageListApi.as_view(), name='image_list'),
    path('image-delete/<pk>', views.ImageDelete.as_view(), name='image_delete'),
    path('image-detail/<pk>', views.UserImageDetail.as_view(), name='image_detail'),
    path('image-filter/<name>',views.UserImageFilterByName.as_view(), name='image_filter'),


]
