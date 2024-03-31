from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, UpdateView, DeleteView
import os
from datetime import datetime
from .forms import MainForm
from .models import MyModel


# Create your views here.
def index(request):
    data = MyModel.objects.order_by('-name')
    return render(request, 'main/index.html', {'data': data})


class MessageDetailView(DetailView):
    model = MyModel
    template_name = 'main/view_message.html'
    context_object_name = 'message_view'


class MessageUpdateView(UpdateView):
    model = MyModel
    template_name = 'main/message.html'
    form_class = MainForm


class MessageDeleteView(DeleteView):
    model = MyModel
    success_url = '/'
    template_name = 'main/delete.html'


def message(request):
    errors = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            errors = 'Форма заполнена неверно'

    form = MainForm()

    data = {
        'form': form,
        'errors': errors
    }

    return render(request, 'main/message.html', data)


def pages(request):
    data = {
        'values': [
            f"{reverse('index')} - Главная страница",
            f"{reverse('message')} - Сообщения",
            f"{reverse('pages')} - Страницы",
            f"{reverse('time_now')} - Текущее время",
            f"{reverse('directory')} - Каталог"
        ]
    }
    return render(request, 'main/pages.html', data)


def time_now(request):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    data = {
        'values': [f'Год: {year}', f'Месяц: {month}', f'День: {day}', f'Час: {hour}', f'Минута: {minute}']
    }
    return render(request, 'main/time_now.html', data)


def directory(request):
    workdir = os.getcwd()
    data = {'values': os.listdir(workdir)}
    return render(request, 'main/directory.html', data)