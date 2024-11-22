from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.DirectorListCreateView),
    path('directors/<int:id>/', views.DirectorDetailView),
    path('movies/', views.MovieListCreateView),
    path('movies/<int:id>/', views.MovieDetailView),
    path('movies/reviews/', views.MovieReviewsListView),
    path('reviews/', views.ReviewListCreateView),
    path('reviews/<int:id>/', views.ReviewDetailView),]