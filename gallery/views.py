from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.http.response import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from gallery.models import Photos, Comments
from loginsys.models import Account
import json
import bleach

def main(request, **kwargs):
	args = {}
	if kwargs.get('login_error') is not None:
		args['login_error'] = True
	photos = Photos.objects.all()
	args.update(csrf(request))
	if request.user.is_authenticated():
		args['signed_in'] = True
		args['user'] = auth.get_user(request)
	args['photo_1'] = photos[0]
	args['photo_2'] = photos[1]
	args['photo_3'] = photos[2]
	args['photo_4'] = photos[3]
	args['comments'] = Comments.objects.all()
	return render_to_response('gallery.html', args)

def getComments(request):
	data = []
	photoURL = request.GET['photoURL']
	allComments = Comments.objects.all()
	for comment in allComments:
		if comment.commentPhoto.photo == photoURL:
			data.append((comment.commentText, comment.user.username))
	return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8')

def addComment(request):
	user = auth.get_user(request)
	if not request.user.is_authenticated():
		return main(request, login_error=True)
	if request.POST:
		photo = Photos.objects.get(photo=request.POST['photoURL'])
		message = request.POST['message']
		message = bleach.clean(message)
		comment = Comments.objects.create(user=user, commentText=message, commentPhoto=photo)
		comment.save()
	return redirect('/gallery/')

def addLike(request):
	user = auth.get_user(request)
	data = {}
	data['username'] = user.username
	photoURL = request.GET['photoURL']
	photo = Photos.objects.get(photo=photoURL)
	liked = photo.liked
	user_ids = Photos.objects.values_list('liked', flat=True).filter(photo=photoURL)
	print(user_ids)
	was = False
	for user_id in user_ids:
		if not user_id == None:
			if Account.objects.get(id=user_id) == user:
				liked.remove(user)
				was = True
				break
	if not was:
		liked.add(user)
	data['count'] = len(liked.all())
	return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8')

def getLikes(request):
	data = {}
	photoURL = request.GET['photoURL']
	photo = Photos.objects.get(photo=photoURL)
	liked = photo.liked
	data['count'] = len(liked.all())
	return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8')