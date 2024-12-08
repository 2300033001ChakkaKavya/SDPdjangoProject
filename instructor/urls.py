from django.urls import path, include
from . import views
app_name = 'instructor'

urlpatterns = [
    path('instructorhomepage/',views.instructorhomepage,name="instructorhomepage"),
    path('view_assignments/', views.view_assignments,name='view_assignments'),
    path('viewAssignment/', views.viewAssignment,name='viewAssignment'),
    path('addAssignment/', views.addAssignment, name='addAssignment'),
    path('add_assignment/', views.add_assignment,name='add_assignment'),
    path('add-assignment/<int:course_id>/', views.add_assignment, name='add_assignment'),
]