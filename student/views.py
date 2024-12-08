from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddCourseForm

from django.contrib.auth.decorators import login_required

# Student Homepage
def studenthomepage(request):
    return render(request, 'student/StudentHomePage.html')

# Add Course
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:studenthomepage')
    else:
        form = AddCourseForm()
    return render(request, 'student/add_course.html', {'form': form})


def coursematerial(request):
    return render(request, 'student/coursematerial.html')

def c(request):
    return render(request, 'student/c.html')
def cplus(request):
    return render(request, 'student/cplus.html')
def python(request):
    return render(request, 'student/python.html')
def java(request):
    return render(request, 'student/java.html')
def html(request):
    return render(request, 'student/html.html')

def get_videos():
    # This is an example. Modify this to fetch your videos from a database or static files.
    return [
        {'title': 'Video 1', 'url': 'https://www.youtube.com/watch?v=rHux0gMZ3Eg'},
        {'title': 'Video 2', 'url': 'https://www.example.com/video2'},
    ]
def video_gallery(request):
    videos = get_videos()  # Assuming you have a function to fetch videos
    return render(request, 'student/view_gallery.html', {'videos': videos})


def quizpage(request):
    return render(request, 'student/QuizPage.html')

from django.shortcuts import render, get_object_or_404
from .models import Quiz

def attempt_quiz(request, quiz_id):
    """
    View to handle displaying a quiz for a given quiz_id.
    """
    # Replace Quiz with your model name if it's different
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # You can fetch questions for this quiz from a related model (e.g., quiz.questions.all())
    questions = quiz.questions.all()  # Assuming a ForeignKey/ManyToMany relationship

    return render(request, 'QuizPage.html', {'quiz': quiz, 'questions': questions})


