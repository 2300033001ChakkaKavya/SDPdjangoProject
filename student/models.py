from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'ADVANCED OBJECT-ORIENT PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),

    ]
    SECTION_CHOICES = [
        ('S11', 'SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
        ('S16', 'SECTION S16'),
    ]
    course = models.CharField(max_length=50,choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)


class YouTubeVideo(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    video_url = models.URLField()  # Stores the YouTube video link
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.title


from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Default description")

    def _str_(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def _str_(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def _str_(self):
        return self.text


