from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Item
from django.contrib  import messages
from ..loginRegister.models import User

# Create your views here.
def delete(request, id):
	destroy = Item.objects.get(id=id)
	destroy.delete()
	return redirect('my_login_home')

def remove(request, id):
	if "id" not in request.session:
		return redirect("my_login_index")
	
	item = Item.objects.get(id=id)
	user = User.objects.get(id=request.session["id"])

	item.userswant.remove(user)

	return redirect("my_login_home")

def show(request, id):
	if "id" not in request.session:
		return redirect("my_login_index")
	context = {
		"item": Item.objects.get(id=id)
	}
	return render(request, "blackbeltTemp/show.html", context)

def new(request):
	if "id" not in request.session:
		return redirect("my_login_index")

	return render(request, "blackbeltTemp/new.html")

def add_to_wishlist(request, id):
	if "id" not in request.session:
		return redirect("my_login_index")
	
	item = Item.objects.get(id=id)
	user = User.objects.get(id=request.session["id"])

	item.userswant.add(user)

	return redirect("my_login_home")

def create(request):
	if request.method != 'POST':
		return redirect('create_item')
	# user = User.objects.get(id=request.session["id"])
	data = {
		"user": User.objects.get(id=request.session["id"])
	}
	results = Item.itemManager.isValidAdd(request.POST, data)
	if results[0]:
		return redirect(reverse('my_login_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.error(request, error)
		return redirect(reverse('new_item'))



