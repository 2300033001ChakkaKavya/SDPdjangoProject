from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['course', 'section']


from .models import YouTubeVideo

class YouTubeVideoForm(forms.ModelForm):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'video_url', 'description']