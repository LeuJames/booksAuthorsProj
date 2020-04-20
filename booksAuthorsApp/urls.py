from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('submitBook', views.submitBook),
    path('addAuthor', views.addAuthor),
    path('submitAuthor', views.submitAuthor),
    path('book/<int:id>', views.book),
    path('author/<int:id>', views.author),
    path('authorAddBook', views.authorAddBook),
    path('bookAddAuthor', views.bookAddAuthor),
]
