from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect



def UserHomePage(request):
    return render(request, 'userapp/UserHomePage.html')


def UserLoginPageCall(request):
    return render(request, 'userapp/Login.html')

def UserRegisterpagecall(request):
    return render(request, 'userapp/RegisterPage.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def UserRegisterLogic(request):
    if request.method == 'POST':
        # Get form data
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Split fullname into first_name and last_name
        first_name, *last_name_parts = fullname.split(' ', 1)
        last_name = last_name_parts[0] if last_name_parts else ''

        # Validate password match
        if password == confirm_password:
            # Check if username or email is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'OOPS! Username already taken.')
                return render(request, 'RegisterPage.html')  # Ensure this template exists
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'OOPS! Email already registered.')
                return render(request, 'RegisterPage.html')  # Ensure this template exists
            else:
                # Create a new user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('UserHomePage')  # Replace 'homepage' with the correct URL name for your homepage
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'RegisterPage.html')  # Ensure this template exists
    else:
        return render(request, 'RegisterPage.html')  # Ensure this template exists




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def UserLogoutLogic(request):
    # Log out the user
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')  # Redirect to the login page after logout

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('student:studenthomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:

                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('instructor:instructorhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'userapp/Login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'userapp/Login.html')
    else:
        return render(request, 'userapp/Login.html')






from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return render(request, 'userapp/UserHomePage.html', {
                'form': FeedbackForm(),  # Provide a blank form after submission
                'message': 'Thank you for your feedback!',
            })
    else:
        form = FeedbackForm()

    return render(request, 'userapp/feedback.html', {
        'form': form,
    })


