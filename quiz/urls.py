

from django.urls import path
from . import views

urlpatterns = [
        
    path('', views.dashboard, name='dashboard'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/attempt/', views.quiz_attempt, name='quiz_attempt'),
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
    path('logout/', views.user_logout, name='logout'),
    
    # path('profile/', views.user_profile, name='user_profile'),
    
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
   
    path('participant/', views.participant_list, name='participant_list'),
   # path('participant/search/', views.searchparticipant, name='searchparticipant'),
    path('participant/', views.participant_list, name='participant_list'),





]



 