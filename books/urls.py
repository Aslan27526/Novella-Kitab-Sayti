
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books import views
app_name = 'books'
urlpatterns = [

    path('', views.index.as_view(), name='index'),
    path('about/', views.about, name="about"),
    path('detail/<int:id>', views.detail.as_view(), name='detail'),
    path('categories/<janr>', views.categories.as_view(), name='categories'),
    path('<int:fav_id>/favourite_post/',
         views.favourite_post, name='favourite_post'),

    path('favourites/', views.favorite_list, name='favorite_list')



]
