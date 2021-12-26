from django.shortcuts import render, redirect, get_object_or_404

# message불러올때
from django.contrib import messages

# decorator 불러들일때
from django.contrib.auth.decorators import login_required

# Model, Form 불러올때
from .forms import PythonForm
from .models import Python
from course.models import Course

# Create your views here.
def pyHome(request):
    pyList = Python.objects.all()
    # item = Python.objects.get(id=1)
    item = Course.objects.get(id=1)

    data = {
        'pyList': pyList,
        'item': item,
    }

    return render(request, 'python/pyHome.html', data)

# @login_required
def pyAdd(request):

    if request.method == 'POST':
        form = PythonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "New Python was successfully added!")
            return redirect('python:pyHome')

    else:
        form = PythonForm()
        data = {
            'form' : form,
            # 'csrfmiddlewaretoken': '{{ csrf_token }}',
        }
    return render(request, 'python/pyForm.html', data)

def pyEdit(request, py_id):
    pyList = Python.objects.all()
    item = get_object_or_404(Python, pk=py_id)

    data = {
        'pyList' : pyList,
        'item' : item,
    }

    return render(request, 'python/pyEdit.html', data)

def pyReform(request, py_id):

    item = get_object_or_404(Python, pk=py_id)

    if request.method == 'POST':
        form = PythonForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'New python was successfully edited!')
            return redirect('python:pyHome')

    else:
        form = PythonForm(instance=item)
        data ={
            'form' : form,
        }
    return render(request, 'python/pyForm.html', data)


##For TEST ##############################################################
def pyTest(request):
    ###############################





    ################################
    return render(request, 'python/pyHome.html')



###End TEST#########################################################################