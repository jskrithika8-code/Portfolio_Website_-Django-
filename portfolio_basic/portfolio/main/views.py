from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    projects = [
        {'title': 'Weather CLI',      'desc': 'CLI weather app using Open-Meteo API.',       'tech': 'Python',        'url': '#'},
        {'title': 'Expense Tracker',  'desc': 'Track expenses with CSV & JSON storage.',      'tech': 'Python, Tkinter','url': '#'},
        {'title': 'File Organizer',   'desc': 'Auto-organize files into category folders.',   'tech': 'Python',        'url': '#'},
        {'title': 'Portfolio Website','desc': 'Personal portfolio built with Django.',         'tech': 'Python, Django','url': '#'},
    ]
    skills = ['Python', 'Django', 'Tkinter', 'HTML', 'CSS', 'Git', 'SQL']
    return render(request, 'main/home.html', {'projects': projects, 'skills': skills})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
