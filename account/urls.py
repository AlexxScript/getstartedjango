from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('logout/',views.user_logout,name='logout'),
]