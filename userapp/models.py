from django.db import models

class Feedback(models.Model):
    TOPIC_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    name = models.CharField(max_length=100, blank=True)  # Optional field
    email = models.EmailField(blank=True)  # Optional field
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.name or 'Anonymous'}"


from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Instructor', 'Instructor'),
        ('Student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Custom related name to avoid clash
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Custom related name to avoid clash
        blank=True,
    )
    password = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=150, default='default_user')


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
