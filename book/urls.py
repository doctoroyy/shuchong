from django.contrib import admin
from django.urls import path


from book import views
urlpatterns = [
  path('', views.index, name='index'),
  path('book/download', views.download, name='download'),
  path('book/update', views.update, name='update'),
  path('book/getAll', views.get_all_books, name='get_all_books'),
  path('book/chapter', views.chapter, name='getChapter'),
  path('book/catalog', views.catalog, name='getCatalog'),
  path('book/search', views.search_book, name='searchBook'),
  path('book/register', views.register, name='register'),

  # 历史
  path('catalog/<int:book_id>/', views.catalog2, name='catalog'),
  path('book/<int:book_id>/<int:chapter_no>/', views.chapter_detail, name='chapter_detail'),

]
