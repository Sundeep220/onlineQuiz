from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view_score', views.view_score,name="view_score"),
    path('api/check_score', views.check_score, name="check_score"),
    path('leaderboard', views.leaderboard,name="leaderboard"),
    path('<id>' , views.take_quiz, name="quiz"),
    path('api/<id>', views.get_quiz, name="get_quiz")
]
