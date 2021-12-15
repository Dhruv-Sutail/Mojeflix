from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.HomeView.as_view(),name="home"),
   path('login/',views.LoginView.as_view(),name="login"),
   path('register/',views.RegisterView.as_view(),name="register"),
   path("profile/", views.LoginSuccess.as_view() , name="profile"),
   path('profile/<slug:slug>',views.VideoPlayerView.as_view(),name="videoplayer"),
   path('success/',views.success,name="success"),
   path("logout/",views.LogoutView.as_view(),name="logout")
]
