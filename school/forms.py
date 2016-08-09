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
	message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 3}), help_text='160')
	audience_ind = forms.CharField(label = 'Audience Individuals')
	audience_grp = forms.CharField(label = 'Audience Groups')
   	class Meta:
   		model = Message
   		fields = ('audience_ind', 'audience_grp', 'message', 'date')

