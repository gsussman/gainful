from django import forms

from .models import Student, Group, Message
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'email')

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'member')

class MessageForm(forms.ModelForm):
	date = forms.SplitDateTimeField()
   	class Meta:
   		model = Message
   		fields = ('audience_ind', 'audience_grp', 'message', 'date')