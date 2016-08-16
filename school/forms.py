from django import forms

from .models import Student, Group, Message
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.safestring import mark_safe

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'email')

class GroupForm(forms.ModelForm):
#    member = forms.ModelMultipleChoiceField(help_text=mark_safe('Hold Command on Windows or Control on Mac to add more users.'))
    class Meta:
        model = Group
        fields = ('name', 'member')
        help_texts = {
            'member': mark_safe('<span style="padding-left: 57px; color: red;"> <br>Hold Command or Control to add or remove members.</span>'),
        }
class MessageForm(forms.ModelForm):
  date = forms.SplitDateTimeField()
  message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 3}), help_text='160')
#	audience_ind = forms.ModelMultipleChoiceField(verbose_name="Audience Individuals")
#	audience_grp = forms.ModelMultipleChoiceField(verbose_name="Audience Groups")
  class Meta:
    model = Message
    fields = ('audience_Individuals', 'audience_Groups', 'message', 'date')
    help_texts ={
    'audience_Individuals': mark_safe('<span style="color: red;"> <br>Hold Command or Control to add or remove members.</span>'),
    'audience_Groups': mark_safe('<span style="color: red;"> <br>Hold Command or Control to add or remove groups.</span>'),
    }