from django import forms
from .models import Assignment, Course


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'course', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter assignment title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter assignment description',
                'rows': 5
            }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

    def _init_(self, *args, **kwargs):
        instructor = kwargs.pop('instructor', None)
        super()._init_(*args, **kwargs)
        # Limit the course dropdown to courses taught by the instructor
        if instructor:
            self.fields['course'].queryset = instructor.course_set.all()

