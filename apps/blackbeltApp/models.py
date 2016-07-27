from __future__ import unicode_literals
from django.db import models
from ..loginRegister.models import User

# Create your models here.
class ItemManager(models.Manager):
	def isValidAdd(self, context, data):
 		errors = [] 
 		passflag = True
 		if len(context['name']) < 3:
			errors.append("Item name must have at least 3 characters!")
			passflag = False

		if passflag == True:
			self.create(name = context['name'], creator = User.objects.get(id=data['user'].id))
		return [passflag, errors]

class Item(models.Model):
	name = models.CharField(max_length=255)
	creator = models.ForeignKey(User, related_name="creator")
	userswant = models.ManyToManyField(User, related_name="userswant")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	itemManager = ItemManager()
	objects = models.Manager()







