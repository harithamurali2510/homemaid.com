from django.db import models

# Create your models here.
class MaidSignUp(models.Model):
	cusrname = models.CharField(blank=True , max_length=20)
	cpassword = models.CharField(blank=True , max_length=20)
	distcode = models.CharField(blank=True , max_length=20)
	username = models.CharField(blank=True , max_length=20)
	password = models.CharField(max_length=10)

	name = models.CharField(blank=True , max_length=20)
	age = models.IntegerField(blank=True, default=0)
	gender = models.CharField(blank=True , max_length=10)
	address = models.CharField(blank=True , max_length=100)
	phone = models.IntegerField(blank=True, default=0 )
	field = models.CharField(blank=True , max_length=15)
	work_type = models.CharField(blank=True , max_length=15)
	availability = models.CharField(blank=True, max_length=10)
	uploaded_file_url =  models.CharField(blank=True, max_length=10)
	imagename = models.CharField(blank=True, max_length=10)

	def __unicode__(self):
		return self.username

class ClientSignUp(models.Model):
	username = models.CharField(blank=True , max_length=20)
	password = models.CharField(max_length=10)

	name = models.CharField(blank=True , max_length=20)
	email = models.EmailField( blank=False)
	age = models.IntegerField(blank=True, default=0 )
	gender = models.CharField(blank=True , max_length=10)
	address = models.CharField(blank=True , max_length=100)
	phone = models.IntegerField(blank=True, default=0 )

	def __unicode__(self):
		return self.username

class Akshaya(models.Model):
	centre_name = models.CharField(blank=True, max_length=30)
	distcode = models.CharField(blank=True, max_length=30)
	passcode = models.CharField(blank=True, max_length=30)
	contact = models.IntegerField(blank=False, default =0)
	
	def __unicode__(self):
		return self.centre_name

