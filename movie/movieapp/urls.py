from movieapp import *
from django.urls import path
from .views import *

urlpatterns=[
    path('', MovieGetCreate.as_view()),
    path('<int:pk>', MovieUpdateDelete.as_view()),
    path('', GenreGetCreate.as_view()),
    path('<int:pk>', GenreUpdateDelete.as_view()),
]