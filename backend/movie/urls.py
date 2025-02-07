from movie import views
from django.urls import path
from .views import MovieCreate, MovieUpdateDelete

urlpatterns=[
    path('', MovieCreate.as_view()),
    path('<int:pk>', MovieUpdateDelete.as_view()),
    
]