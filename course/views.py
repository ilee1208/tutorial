from django.shortcuts import render, redirect, get_object_or_404

# message불러올때
from django.contrib import messages

from .forms import CourseForm
from .models import Course

# decorator 불러들일때
from django.contrib.auth.decorators import login_required

# Create your views here.
def courseHome(request):
    courseList = Course.objects.all()
    item = Course.objects.get(id=1)

    data = {
        'courseList': courseList,
        'item': item,
    }

    return render(request, 'course/courseHome.html', data)

def courseAdd(request):

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "New Course was successfully added!")
            return redirect('main:index')

    else:
        form = CourseForm()
        data = {
            'form' : form,
            # 'csrfmiddlewaretoken': '{{ csrf_token }}',
        }
    return render(request, 'course/courseForm.html', data)


def courseEdit(request, course_id):
    courseList = Course.objects.all()
    item = get_object_or_404(Course, pk=course_id)

    data = {
        'courseList' : courseList,
        'item' : item,
    }

    return render(request, 'course/courseEdit.html', data)

def courseReform(request, course_id):

    item = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'New course was successfully edited!')
            return redirect('main:index')
    else:
        form = CourseForm(instance=item)
        data ={
            'form' : form,
            'course_id' : course_id
        }
    return render(request, 'course/courseForm.html', data)


def bootstrap(request):
    return render(request, 'course/bootstrap.html')
