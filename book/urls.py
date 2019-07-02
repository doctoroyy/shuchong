from django.contrib import admin
from django.urls import path

from book import views

urlpatterns = [
  path('', views.index, name='index'),
  path('book/<int:book_id>/<int:chapter_no>/', views.chapter_detail, name='chapter_detail'),
  path('download/', views.download, name='download'),
  path('catalog/<int:book_id>/', views.catalog, name='catalog'),
  path('catalogtojson/<int:book_id>/', views.catalogtojson, name='catalogtojson'),

  path('demo/', views.demo, name='demo'),
  path('getAll/', views.get_all_books, name='get_all_books')
]
