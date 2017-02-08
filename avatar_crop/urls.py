from django.conf.urls import url
from avatar_crop.views import avatar_crop

urlpatterns = [
    url(r'^crop/(\d+)/$', avatar_crop, name='avatar_crop'),
    url(r'^crop/$', avatar_crop, name='avatar_crop_default'),
]
