from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Employee




def login_view(request):
    if request.method == 'POST':
        empid = request.POST['empid']
        emppasswd = request.POST['emppasswd']

        try:
            employee = Employee.objects.get(empid=empid)
            if check_password(emppasswd, employee.emppasswd):
                # ロールに応じたメニュー画面にリダイレクト
                if employee.emprole == 0:  # 管理者
                    return redirect('admin_home.html')
                elif employee.emprole == 1:  # 従業員
                    return redirect('employee_home.html')
                elif employee.emprole == 2:  # 医師
                    return redirect('doctor_home.html')
                else:
                    messages.error(request, '無効なユーザーロールです。')
            else:
                messages.error(request, 'ユーザーIDまたはパスワードが違います。')
        except Employee.DoesNotExist:
            messages.error(request, 'ユーザーIDまたはパスワードが違います。')

    return render(request, 'login.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def employee_home(request):
    return render(request, 'employee_home.html')

def doctor_home(request):
    return render(request, 'doctor_home.html')
