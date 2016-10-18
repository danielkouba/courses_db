from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
	courses = Course.objects.all()
	return render(request, 'courses_app/index.html', context = {'courses': courses})

def newcourse(request):
	description = Description.objects.create(content=request.POST['coursedescription']);
	name = request.POST['coursename']
	Course.objects.create(name=name, description=description);
	return redirect('/')

def delete(request, courseID):
	course = Course.objects.get(id=courseID)
	return render(request, 'courses_app/delete.html', context = {'course': course})

def processdelete(request, courseID):
	toBeDeleted = Course.objects.get(id=courseID)
	toBeDeleted.delete()
	return redirect('/')