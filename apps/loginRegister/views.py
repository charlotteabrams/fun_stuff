from django.shortcuts import render, redirect
from .models import User, UserManager
from ..blackbeltApp.models import Item
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse

####################################################

# PROCESSING DATA 

####################################################

def processregister(request):
	if request.method != "POST":
		return redirect("my_login_index")
	results = User.userManager.isValidReg(request.POST)
	errors = results[1]
	for error in errors:
		messages.error(request, error)

	if results[0]:
		return redirect(reverse('my_login_home'))
	else: 
		return redirect(reverse('my_login_register'))

def processlogin(request):
	if request.method != "POST":
		return redirect("my_login_index")
	results = User.userManager.validlog(request.POST)
	print request.POST['username']
	if results[0]:
		request.session['id'] = results[1].id
		request.session['username'] = results[1].username
		return redirect(reverse('my_login_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_login_index'))





####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'travelAppTemplates/index.html')

def home(request):
	print Item.objects.all()
	if "id" not in request.session:
		return redirect("my_login_index")
	user = User.objects.get(id=request.session["id"])
	context={
		"items_on": Item.objects.filter(creator=user) | Item.objects.filter(userswant__id=user.id),
		"items_off": Item.objects.exclude(creator=user).exclude(userswant__id=user.id),
		'name': user.username,
		'first_name': user.name
	}
	return render(request, 'travelAppTemplates/home.html', context)

def register(request):
	return render(request, 'travelAppTemplates/registration.html')

def userProfile(request):
	if "id" not in request.session:
		return redirect("my_login_index")
	return render(request, 'travelAppTemplates/userProfile.html')



 
def logout(request):
	request.session.clear()
	return redirect(reverse('my_login_index'))

