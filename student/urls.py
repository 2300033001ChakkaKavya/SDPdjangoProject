from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('studenthomepage/', views.studenthomepage, name='studenthomepage'),
    path('add_course/', views.add_course, name='add_course'),
    path('coursematerial/', views.coursematerial, name='coursematerial'),
    path('c/', views.c, name='c'),
    path('cplus/', views.cplus, name='cplus'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('html/', views.html, name='html'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('get_videos/', views.get_videos, name='get_videos'),
    path('quiz/', views.quizpage, name='quizpage'),
    path('attempt_quiz/', views.attempt_quiz, name='attempt_quiz')

]
