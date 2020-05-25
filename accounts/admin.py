from django.contrib import admin


# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student)
admin.site.register(Word)
admin.site.register(Lesson)

