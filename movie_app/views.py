from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer,DirectorDetailSerializer, MovieSerializer,
                          MovieDetailSerializer, ReviewSerializer,ReviewDetailSerializer)

# Directors views
@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_detail(request, id):
    director = get_object_or_404(Director, id=id)
    data = DirectorDetailSerializer(director).data
    return Response(data=data)

# Movies views
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    data = MovieDetailSerializer(movie).data
    return Response(data=data)

# Movies with reviews and ratings views
@api_view(['GET'])
def movie_reviews_list(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

# Reviews views
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)