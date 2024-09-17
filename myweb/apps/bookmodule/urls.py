# apps/bookmodule/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.index, name='book_view'),
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    
]
