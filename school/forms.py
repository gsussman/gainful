from django import forms

from .models import Student, Group, Message
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.safestring import mark_safe
from django_select2.forms import Select2Widget, Select2MultipleWidget

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
  message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 3}), help_text=mark_safe('<span class="countdown">160</span>'), label='Custom Message')
  class Meta:
    model = Message
    fields = ('audience_Individuals', 'audience_Groups', 'message', 'date')

#    widgets = {
#      'audience_Groups': Select2MultipleWidget(attrs={'placeholder': 'This is some placeholder text'}),
#      }