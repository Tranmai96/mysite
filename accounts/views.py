from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import LessonForm

# Create your views here.

def home(request):
    words=Word.objects.all()
    total_words=words.count()
    students=Student.objects.all()
    lessons = Lesson.objects.all()
    passed = lessons.filter(status='合格').count()
    pending = lessons.filter(status='Pending').count()
    total_lessons = lessons.count()

    context = { 'words':words, 'students':students,
	'total_words':total_words,'passed':passed,
	'pending':pending,'lessons':lessons,'total_lessons':total_lessons }
    return render(request, 'accounts/dashboard.html', context)


def word(request):
    words=Word.objects.all()
    total_words=words.count()
    students=Student.objects.all()
    lessons = Lesson.objects.all()
    total_lessons = lessons.count()
    passed = lessons.filter(status='合格').count()
    pending = lessons.filter(status='Pending').count()

    context = { 'words':words, 'students':students,
	'total_words':total_words,'passed':passed,
	'pending':pending,'lessons':lessons }

    return render(request, 'accounts/word_list.html', context)

def student(request, pk):
    student= Student.objects.get(id=pk)
    lessons = student.lesson_set.all()
    total_lessons=lessons.count()
    passed = lessons.filter(status='合格').count()
    pending = lessons.filter(status='Pending').count()

    context = {'student':student,'passed':passed,
    'pending':pending,'lessons':lessons}
    return render(request, 'accounts/student.html',context)

def createLesson(request):
    form = LessonForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form} 
    return render(request, 'accounts/lesson_form.html',context)

# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
    
# 	order_count = orders.count()

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
# 	return render(request, 'accounts/customer.html',context)