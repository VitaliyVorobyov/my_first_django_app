from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
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
