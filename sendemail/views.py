from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            cd = contactForm.cleaned_data
            subject = cd['subject']
            message = cd['message']
            from_email = cd['from_email']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('success')
    else:
        contactForm = ContactForm()
    return render(request, 'sendemail/email.html', {'contactForm': contactForm})


def successView(request):
    return render(request, 'sendemail/success.html')

