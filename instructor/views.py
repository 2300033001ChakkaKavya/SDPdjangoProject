from django.shortcuts import render





def instructorhomepage(request):
    return render(request, 'instructor/InstuctorHomePage.html')


from django.contrib.auth.decorators import login_required
from .forms import AssignmentForm

@login_required
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor:instructorhomepage')  # Redirect back to the add assignment page
    else:
        form = AssignmentForm()

    return render(request, 'instructor/AddAssignment.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Assignment, Course

def view_assignments(request):
    if not request.user.is_authenticated:  # Check if user is logged in
        return redirect('login')  # Redirect to the login page if not authenticated

    if hasattr(request.user, 'role'):  # Ensure the user has a 'role' attribute
        if request.user.role == 'Instructor':
            assignments = Assignment.objects.filter(course__instructor=request.user)
        elif request.user.role == 'Student':
            courses = Course.objects.filter(enrollment__student=request.user)
            assignments = Assignment.objects.filter(course__in=courses)
        else:
            assignments = []  # For users without a valid role
    else:
        return redirect('instructor:viewAssignment')  # Redirect if user model is misconfigured

    return render(request, 'instructor/View_Assignments.html', {'assignments': assignments})



def addAssignment(request):
    return render(request, 'instructor/AddAssignment.html')

def viewAssignment(request):
    return render(request, 'instructor/View_Assignment.html')


