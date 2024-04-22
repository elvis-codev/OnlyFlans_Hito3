from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactFormForm
from .models import Flan, ContactForm
from django.contrib import messages

# Create your views here.
def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            messages.success(request, '¡El formulario se ha enviado con éxito!')
            return redirect('contacto')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})


def exito(request):
    return render(request, 'success.html', {})