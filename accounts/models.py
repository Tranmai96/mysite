from django.db import models


# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name



class Word(models.Model):

	word = models.CharField(max_length=200, null=True)
	definition = models.TextField(null=True)
	example = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.word




class Lesson(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('合格', '合格'),
			)

	student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
	word = models.ForeignKey(Word, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.word.word
