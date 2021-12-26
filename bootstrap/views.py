from django.shortcuts import render, redirect, get_object_or_404

# message불러올때
from django.contrib import messages

# decorator 불러들일때
from django.contrib.auth.decorators import login_required

# Model, Form 불러올때
from .forms import BsForm
from .models import Bs

# Create your views here.
def bsHome(request):
    bsList = Bs.objects.all()
    item = Bs.objects.get(id=1)

    data = {
        'bsList': bsList,
        'item': item,
    }
    return render(request, 'bootstrap/bsHome.html', data)

# @login_required
def bsList(request):
    bsList = Bs.objects.all()
    item = Bs.objects.get(id=1)

    data = {
        'bsList': bsList,
        'item': item,
    }
    return render(request, 'bootstrap/bsList.html')

@login_required
def bsAdd(request):

    if request.method == 'POST':
        form = BsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "New BS was successfully added!")
            return redirect('bootstrap:bsHome')

    else:
        form = BsForm()
        data = {
            'form' : form,
            # 'csrfmiddlewaretoken': '{{ csrf_token }}',
        }
    return render(request, 'bootstrap/bsForm.html', data)



def bsEdit(request, bs_id):
    bsList = Bs.objects.all()
    item = get_object_or_404(Bs, pk=bs_id)

    data = {
        'bsList' : bsList,
        'item' : item,
    }

    return render(request, 'bootstrap/bsEdit.html', data)

def bsReform(request, bs_id):

    item = get_object_or_404(Bs, pk=bs_id)

    if request.method == 'POST':
        form = BsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'New boostrap was successfully edited!')
            return redirect('bootstrap:bsHome')

    else:
        form = BsForm(instance=item)
        data ={
            'form' : form,
        }
    return render(request, 'bootstrap/bsForm.html', data)
