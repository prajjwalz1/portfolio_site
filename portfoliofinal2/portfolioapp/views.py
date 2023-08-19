# Import the necessary Django libraries
from django.shortcuts import render, redirect
from .models import about,fact,skills,Resumes,workhistory,webresponsibilities,designer_responsibilities,portfolio,services,testimonial,contact
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def home(request):
    abouts=about.objects.all()
    facts=fact.objects.all()
    skill=skills.objects.all()
    resume=Resumes.objects.all()
    workhistories=workhistory.objects.all()
    webresponsibility=webresponsibilities.objects.all()
    designer_responsibility=designer_responsibilities.objects.all()
    portfolios=portfolio.objects.all()
    service=services.objects.all()
    testimonials=testimonial.objects.all()
    contactss=contact.objects.all()



    return render(request, 'index.html',{'details':abouts, 'skills':skill, 'facts':facts, 'resumes':resume,'workhistories':workhistories,'webresponsibilities':webresponsibility,'designer_responsibilities':designer_responsibility,'portfolio':portfolios,'services':service,'testimonial':testimonials,'contact':contactss})

def projects(request):
    return render(request, 'projects.html')


# @csrf_exempt
@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = "Name: {}\n\n{}".format(name, message)

        try:
            send_mail( subject, full_message, email, ['acharyaprajjwol152@gmail.com'])
            messages.success(request, 'Your message has been sent. Thank you!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect(reverse('home'))
        else:
            return redirect(reverse('home') + '?success=email sent successfully')
    return redirect('home')