from django.urls import path
from .views import get_all_content





urlpatterns = [
    path('content/', get_all_content),
]


