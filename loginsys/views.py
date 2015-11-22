from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core.mail import send_mail

# Create your views here.

def main(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('main.html', args)


def contact(request):
    sended = True
    if request.method == 'POST':
        contact_name = request.POST.get('contactName')
        contact_email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            send_mail('Email from pestov.me', message + '\n' + contact_email,
                      contact_email, ['grizzlyarchi@gmail.com'])
        except Exception:
            sended = False
    args = {}
    args.update(csrf(request))
    args['emailSended'] = sended
    return render_to_response('main.html', args)
