from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import tracking_numbers
import re

@login_required(login_url='/admin/login')
def index(request):
	refs = tracking_numbers.objects.values()
	csv_refs = ''
	csv_list = []
	for i in refs:
		csv_refs = csv_refs+","+i['tracking_number']
		csv_list.append(i)
	csv_refs = re.sub('^,','',csv_refs)
	context = { 'csv_refs': csv_refs, 'csv_list': csv_list }
	return render(request, 'index.html', context)

def delete(request, id_del):
	ostju = tracking_numbers.objects.get(id=id_del)
	ostju.delete()
	return redirect('/')

def add(request):
	tracking_number = request.POST.get('tracking_number')
	description = request.POST.get('description')
	new_data  =  tracking_numbers(tracking_number=tracking_number, description=description)
	new_data.save()
	return redirect('/')
