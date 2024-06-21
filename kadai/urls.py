from django.urls import path
from .views import login_view, admin_home, employee_home, doctor_home

urlpatterns = [
    path('', login_view, name='login'),
    path('admin_home/', admin_home, name='admin_home'),
    path('employee_home/', employee_home, name='employee_home'),
    path('doctor_home/', doctor_home, name='doctor_home'),
]
