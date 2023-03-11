from django.urls import path
from . import views
from recommendation_api.views import *

urlpatterns = [
    path('crop/', CropApiEndPoint.as_view(), name='crop'),
]