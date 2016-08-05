from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Group, Message

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Message)