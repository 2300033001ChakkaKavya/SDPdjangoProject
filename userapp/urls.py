from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserHomePage, name='UserHomePage'),
    path('UserLoginPageCall/',views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserRegisterpagecall/',views.UserRegisterpagecall, name='UserRegisterpagecall'),
    path('UserRegisterLogic/',views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginLogic/',views.UserLoginLogic, name='UserLoginLogic'),
    path('UserLogoutLogic/',views.UserLogoutLogic, name='UserLogoutLogic'),
    path('feedback', views.feedback, name='feedback'),

]