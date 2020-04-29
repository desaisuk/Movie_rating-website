from django.shortcuts import render, redirect
from .models import Movie, MovieReview
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from django.contrib import messages
from django.db.models import Avg, Func


# To return the average rating value rounded with two decimal places
class Round(Func):
    function = "ROUND"
    arity = 2


# Home view function : This will return the movie details to the user - search movie in the db movie title
def home(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box',None)
        movies = Movie.objects.filter(title__iexact=search_query)
        avg_rating = MovieReview.objects.filter(title__iexact=search_query).aggregate(avg_rating=Round(Avg('rating'),2))
        movie_reviews = MovieReview.objects.filter(title__iexact=search_query)
        total_reviews = MovieReview.objects.filter(title__iexact=search_query).count()
        no_record_flag = False
        if search_query and movies.count() == 0:
            no_record_flag = True

        if movies.count() != 0:
            context = {
                'movies' : movies,
                'movie_avg_rating' : avg_rating,
                'movie_reviews' : movie_reviews,
                'total_reviews' : total_reviews,
            }
            return render(request, 'movie/home.html', context)
        else:
            context = {
                'no_record_flag' : no_record_flag
            }
            return render(request, 'movie/home.html', context)


# About view function
def about(request):
    return render(request, 'movie/about.html')


# Rating view function:
# In GET method return the movie details to the user - search movie in the db movie title
# In POST method submits the response given by user to the db - Movie rating and comment
# Only logged in (registered users) can submit the response
@login_required
def rating(request):

    if request.method == "GET":
        search_query = request.GET.get('search_box1',None)
        movies = Movie.objects.filter(title__iexact=search_query)
        form = RatingForm(initial={'title':search_query})
        no_record_flag = False
        if search_query and movies.count() == 0:
            no_record_flag = True
        if movies.count() != 0:
            context = {
                'movies' : movies,
                'form' : form
            }
            return render(request, 'movie/rating.html', context)
        else:
            context = {
                'no_record_flag' : no_record_flag
            }
            return render(request, 'movie/rating.html', context)

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            print("Valid form")
            form.save()
            messages.success(request, f'Your review has been added!')
            return redirect('movie-home')
        
        else:
            title = request.body.decode('utf-8').split('&')[1].split('=')[1].replace('+',' ')
            print("Not valid")
            movies = Movie.objects.filter(title__iexact=title)
            context = {
                'movies' : movies,
                'form' : form
            } 
            return render(request, 'movie/rating.html', context)

        return render(request, 'movie/rating.html', {'form':form}) 
    
     

