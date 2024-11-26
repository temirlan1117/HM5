from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.DirectorListCreateView.as_view),
    path('directors/<int:id>/', views.DirectorDetailView.as_view),
    path('movies/', views.MovieListCreateView.as_view),
    path('movies/<int:id>/', views.MovieDetailView.as_view),
    path('movies/reviews/', views.MovieReviewsListView.as_view),
    path('reviews/', views.ReviewListCreateView.as_view),
    path('reviews/<int:id>/', views.ReviewDetailView.as_view),]