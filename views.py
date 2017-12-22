from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import tracking_numbers
import re

@login_required(login_url='/login')
def index(request):
	refs = tracking_numbers.objects.values().filter(user_id=request.user.id)
	csv_refs = ''
	csv_list = []
	for i in refs:
		csv_refs = csv_refs+","+i['tracking_number']
		csv_list.append(i)
	csv_refs = re.sub('^,','',csv_refs)
	context = { 'csv_refs': csv_refs, 'csv_list': csv_list }
	return render(request, 'index.html', context)

def delete(request, id_del):
	try:
		ostju = tracking_numbers.objects.get(id=id_del, user_id=request.user.id)
	except ObjectDoesNotExist as e:
		ostju = ''
	if ostju:
		ostju.delete()
		return redirect('/')
	else:
		return HttpResponse('<script>javascript:alert("Invalid request.");window.location.assign("/");</script>')

def add(request):
	user_id = request.user.id
	tracking_number = request.POST.get('tracking_number')
	description = request.POST.get('description')
	new_data  =  tracking_numbers(tracking_number=tracking_number, description=description, user_id=user_id)
	new_data.save()
	return redirect('/')

def loginF(request):
	return render(request, 'login.html')

def loginP(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user:
		login(request, user)
		return redirect('/')
	else:
		error_message = "Invalid credentials."
		context = { error_message: 'blablablahhh' }
		return redirect('/', error_message)
