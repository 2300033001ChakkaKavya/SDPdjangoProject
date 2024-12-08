from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('chathomepage/', views.chathomepage, name='chathomepage'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),
]
