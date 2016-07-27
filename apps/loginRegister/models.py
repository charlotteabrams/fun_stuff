from __future__ import unicode_literals
from django.db import models
from django.contrib  import messages
import re
import bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def isValidReg(self, context):
		passflag = True
		errors = []
		password = context['password']
		if len(context['name']) < 3:
			errors.append("Name field must have at least 3 characters!")
			passflag = False
		if len(context['username']) < 3:
			errors.append("Username field must have at least 3 characters!")
			passflag = False
		if len(self.filter(username = context['username'])) > 0:
			errors.append("Username already exists")
			passflag = False 
		if len(context['password']) < 3:
			errors.append("Password cannot be less than 8 characters!")
			passflag = False
		if context['password'] != context['confirm']:
			errors.append("Passwords do not match!")
			passflag = False
  
		if passflag == True:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			self.create(name = context['name'], username = context['username'], password = hashed, datehired = context['date'])
		return [passflag, errors]


	def validlog(self, context):
 		errors = [] 
 		passflag = False
 		if len(self.filter(username = context['username'])) < 1:
 			errors.append('Invalid login')
		if len(self.filter(username = context['username'])) > 0:
			guy = self.get(username = context['username'])
			# guy = self.filter(username = context['username'])
			# guy=guy[0]
			hashed = guy.password
			hashed = hashed.encode('utf-8')
			password= context['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				passflag = True
			else:
				errors.append("Invalid login")
		if not passflag:
			return [passflag, errors]
		return [passflag, guy]





class User(models.Model):
	name = models.CharField(max_length = 255)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=255)
	datehired = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	objects = models.Manager()


