from django.urls import path
from .views import *

urlpatterns = [
    path("add/",create_short_url.as_view(),name="shorten_url"),
    path("up/<str:short_code>",update_short_url.as_view(),name="update or delete url"),
    path("long/<str:short_code>",get_long_url.as_view(),name="get the long url"),
    path("del/<str:short_code>",delete_short_url.as_view(),name="delete the short url")
]
