from django.urls import path
from . import views

urlpatterns = [
    path('title/', views.title.as_view()),
    path('title/<int:pk>/', views.detailtitle.as_view()),
    path('profile/', views.profile.as_view()),
    path('profile/<int:pk>/', views.profiledetail.as_view()),
    path('answers/', views.answer),
    path('question/<int:pk>/', views.question.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)

]