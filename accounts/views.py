from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import LessonForm, StudentForm

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

def vocab_detail(request, pk):
    word= Word.objects.get(id=pk)
    # lesson= word.lesson_set.all()
    # pic = lesson.student.all()
    # status = lesson.status
    # PIC 
    context={'word':word}
    return render(request, 'accounts/vocab_detail.html',context)

def createLesson(request):
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.isvalid():    
            form.save()
            return redirect('/')
       
    context={'form':form} 
    return render(request, 'accounts/lesson_form.html',context)

def addStudent(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect('/')
       
    context={'form':form} 
    return render(request, 'accounts/student_form.html',context)

def updateLesson(request, pk):

	lesson = Lesson.objects.get(id=pk)
	form = LessonForm(instance=lesson)

	if request.method == 'POST':
		form = LessonForm(request.POST, instance=lesson)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/lesson_form.html', context)

def deleteLesson(request, pk):
	lesson = Lesson.objects.get(id=pk)
	if request.method == "POST":
		lesson.delete()
		return redirect('/')

	context = {'item':lesson}
	return render(request, 'accounts/lesson_delete.html', context)



# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
    
# 	order_count = orders.count()

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
# 	return render(request, 'accounts/customer.html',context)