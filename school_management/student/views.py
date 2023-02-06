from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import StudentInsertForm
from .models import Student


# Create your views here.
def dashboard(request, identifier):
    student_info = Student.objects.get(index_number=identifier)
    return HttpResponse('this is student dashboard')


def landing(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('/login/')

    return HttpResponse('loggedindash')
    # if logged in redirect to own student dashboard
    # else redirect to log in


def add(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'student/student_register.html', {'form': StudentInsertForm(), 'title': 'Student'})
