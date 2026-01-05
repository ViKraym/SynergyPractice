from django.shortcuts import render
from .forms import NameForm
from .models import UserName

def home(request):
    greeting = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            UserName.objects.create(name=name)
            greeting = f'Привет, {name}!'
        else:
            greeting = 'Пожалуйста, введите имя.'
    else:
        form = NameForm()
    return render(request, 'greetings/home.html', {'form': form, 'greeting': greeting})