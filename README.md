# Movie Rating and Review website

Movie rating website created using Python and Django web framework which will allow users to check movie information, rating and comments and allow users to give their feedback for a movie.(similar to IMDB)

## Requirements

Python

Django

Cripsy forms (For easy forms styling)



```bash
pip install django-crispy-forms
```

## Functionality provided

 - Guest users would be able to search for a specific movie by movie name.

 - A user is able to Register / Login.

 - Registered users after successful login would be able to rate a movie and comment on it.

 - Admin users would be able to add new movies and its information using default django panel.




## APIs Used

 - API for user Sign Up : User can click on 'Register' link to sign up by providing UserId and Password field.

 - API for user Login : Registered users can login by clicking on 'Login' link, to submit their movie reviews and rating.

 - API for Logout : After providing movie feedback, logged-in users can click on 'Logout' link

 - API to search for a movie : Guest user as well as logged-in users can search for a movie by movie name to get all the information about the movie saved in the database. This search will return the movie description, average movie rating, total number of reviews submitted and all the comments submitted by other users.

- API to rate a movie : Only logged-in user can navigate to 'Rating' url to give feedback about the movie. User need to provide both the fields 'Rating' and 'Comments' as both are mandatory fields. The rating number should be between 1 to 5.


## More Details

- App 'users':

     - Used 'LoginView' and 'LogoutView' provide by 'django.contrib.auth' to implement 'Login' and 'Logout' functionality for users.

     - Used 'UserCreationForm' provide by 'django.contrib.auth.forms' to implement 'User Registration' form.

     - Used 'crispy' forms for easy implementation of form styling


 - App 'movie':

     - Implemented template inheritance functionality provide by Django. 
Code in 'base.html' is inherited in all the required templates.

     - Website will open 'home.html' by default. Guest user can visit the page and search for the movie reviews by providing movie name.

     - Only logged-in users can navigate to the 'rating' url. Added decorator '@login_required' to implement the functionality. If guest user tries to navigate to 'rating' page then it will redirect the user to 'login' page first.

     - Added code to calculate the average of all the ratings submitted by users.

- Database :

     - Created superuser(Admin user) with ID 'TestUser' and password 'testing@123'.
Only this admin user can have access to the Django default admin panel and can add new movies with it's description directly from Django admin panel.

     - Password for all the users is 'testing@123'

     - Added some movies with their descriptions also added some reviews to have basic functionality working.
  
     - Please visit Django admin panel to view all the models and data added
