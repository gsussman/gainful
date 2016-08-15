from django.shortcuts import render, redirect
from .models import Student, Group, Message
from .forms import StudentForm, GroupForm, MessageForm
from datetime import datetime, timedelta
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def overview(request):
	messages_unsent = Message.objects.filter(date__gte=datetime.now())
	messages_sent = Message.objects.filter(date__lt=datetime.now())
	return render(request, 'school/overview.html', {
		'messages_sent' : messages_sent,
		'messages_unsent' : messages_unsent,
		})

def students(request):
	students = Student.objects.all()
	form = StudentForm()
	if request.method == "POST":
		form = StudentForm(request.POST)
    	if form.is_valid():
			post = form.save()
			return redirect('students')
	return render(request, 'school/students.html', {
    'form': form,
    'students': students,
    	})

def groups(request):
	groups = Group.objects.all()
	form = GroupForm()
	if request.method == "POST":
		form = GroupForm(request.POST)
    	if form.is_valid():
			post = form.save()
			return redirect('groups')
	return render(request, 'school/groups.html', {
    'form': form,
    'groups': groups,
    	})

def editgroup(request, id):
	group = Group.objects.get(id = id)
	form = GroupForm(instance=group)
	if request.method == "POST":
		form = GroupForm(request.POST, instance=group)
    	if form.is_valid():
			form.save()
			return redirect('groups')
	return render(request, 'school/group.html', {
    'form': form,
    'group': group,
    	})

def scheduler(request):
	form = MessageForm()
	if request.method == "POST":
		form = MessageForm(request.POST)
		print form
    	if form.is_valid():
			form.save()
			subject = 'New Message Scheduled'
			date = form.cleaned_data['date']
			if form.cleaned_data['audience_Individuals']:
				ind = form.cleaned_data['audience_Individuals']
			else:
				ind = 'No Individuals'
			if form.cleaned_data['audience_Groups']:
				grp = form.cleaned_data['audience_Groups']
			else:
				grp = 'No Groups'
			message = form.cleaned_data['message']
			email = 'Date: %s, Individuals: %s, Groups: %s, Message: %s' % (date, ind, grp, message)
			from_email = 'gainfulio@gmail.com'
			send_mail(subject, email, from_email, ['gene.sussman@gmail.com', 'alicia.morga@gmail.com'])
			return redirect('overview')
	return render(request, 'school/scheduler.html', {
    'form': form,
    	})