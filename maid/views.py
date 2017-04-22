from django.shortcuts import render
from django.conf import settings
from .models import MaidSignUp
from .models import ClientSignUp 
from .models import Akshaya
from django.core.files.storage import FileSystemStorage


# Create your views here.


def home(request):

	return render(request, 'homepages.html', {})

def about(request):
	return render(request, 'aboutus.html')

def homemaid(request):
	data = request.POST
	print 'username: ' + data['usrname']
	print 'password: ' + data['psw']

	is_existing = Akshaya.objects.filter(distcode = data['distcode'] , centre_name = data['cusrname']).exists()

	if is_existing :
		centre = Akshaya.objects.get(distcode = data['distcode'], centre_name = data['cusrname'])
		if centre.passcode == data['cpassword'] :
			is_existing = MaidSignUp.objects.filter(username = data['usrname']).exists()

			if is_existing :
				context = {
				"message" : "Username already exists. " 
				}
				return render (request, 'error.html', context)
			else :	
				form = MaidSignUp()
				form.distcode = data['distcode']
				form.cusrname = data['cusrname']
				form.cpassword = data['cpassword']
				form.username =  data['usrname']
				form.password = data['psw']
				if data['psw'] == data['psw-repeat'] :
					form.save()
					context = {
					"username" : form.username ,
					"password" : form.password
					}
					return render(request, 'maid registration.html', context)
				else :
					context = {
					"message" : " password mismatch " 
					}
					return render (request, 'error.html', context)
		else :
	 		context = {
			"message" : " centre password mismatch " 
			}
			return render (request, 'error.html', context)
	else :
		context = {
		"message" : " invalid centre name " 
		}
		return render (request, 'error.html', context)

	

def homeclient(request):
	data = request.POST
	print 'username: ' + data['usrname']
	print 'password: ' + data['psw']

	is_existing = ClientSignUp.objects.filter(username = data['usrname']).exists()
	if is_existing :
		context = {
		"message" : "Username already exists. " 
		}
		return render (request, 'error.html', context)
	else :
		form = ClientSignUp()
		form.username =  data['usrname']
		form.password= data['psw']
		if data['psw'] == data['psw-repeat'] :
			form.save()
			context = {
				"username" : form.username
			}
			return render(request, 'client registerform.html', context)
		else:
			context = {
			"message" : " password mismatch " 
			}
			return render (request, 'error.html', context)	


def maid_reg(request):
	data = request.POST
	print 'maid'
	form = MaidSignUp.objects.get(username = data['usrname'])
	form.username = data['usrname']
	form.name = data['firstname']
	form.age = data['age']
	form.gender = data['gender']
	form.address = data['address']
	form.phone = data['phone']
	form.field = data['field']
	form.work_type = data['worktype']
	form.availability = data['availability']
	form.save()
	context = {
		"username" : form.username ,
		"name" : form.name ,
		"phone" : form.phone ,
		"address" : form.address ,
		"availability" : form.availability,
		"image" : form.uploaded_file_url
	}
	return render (request, 'mindex.html', context)

def availability(request):
	data = request.POST
	form = MaidSignUp.objects.get(username = data['username'])
	form.availability = data['availability']
	form.save()
	context = {
		"username" : form.username ,
		"name" : form.name ,
		"phone" : form.phone ,
		"address" : form.address,
		"availability" : form.availability
	}
	return render (request, 'mindex.html', context)

def client_reg(request):
	data = request.POST
	print 'client'
	form = ClientSignUp.objects.get(username = data['usrname'])
	form.name = data['firstname']
	form.email= data['email']
	form.age = data['age']
	form.gender = data['gender']
	form.address = data['address']
	form.phone = data['phone']
	form.save()
	context = {
		"name" : form.name ,
		"email" : form.email ,
		"phone" : form.phone ,
		"address" : form.address
	}
	return render (request, 'index.html', context)


def maid_login(request):
	data = request.POST
	print 'username: ' + data['usrname']
	print 'password: ' + data['psw']

	usr = MaidSignUp.objects.get(username= data['usrname'])

	if usr.password == data['psw']:
		context = {
			"username" : usr.username ,
			"name" : usr.name ,
			"phone" : usr.phone ,
			"address" : usr.address
		}
		return render (request, 'mindex.html', context)
	else:

		context = {
			"message" : "password is incorrect" 

		}
		return render (request, 'error.html')


def client_login(request):
	data = request.POST
	print 'username: ' + data['usrname']
	print 'password: ' + data['psw']

	usr = ClientSignUp.objects.get(username= data['usrname'])

	if usr.password == data['psw']:

		context = {
			"name" : usr.name,
			"email" : usr.email,
			"phone" : usr.phone,
			"address" : usr.address
		}
		return render (request, 'index.html', context)
	else:

		context = {
			"message" : "password is incorrect" 

		}
		return render (request, 'error.html', context)


def search(request):
	data = request.POST
	x = data['age']
	age_start, age_end = x.split('-')
	age_list = [int(age_start),int(age_end)]

	usr =  MaidSignUp.objects.filter(gender = data['gender'], age__range = [age_start, age_end], field = data['field'], distcode = data['distcode'], work_type = data['worktype'], availability = "available")
	#for item in usr :
	#	print item.username

	context = {
		"usr" : usr
	} 
	return render(request, 'searchresult (2).html', context)


def results(request):
	data = request.POST

	usr = MaidSignUp.objects.get(username = data['name'])
	context = {
		"name" : usr.name,
		"phone" : usr.phone,
		"address" : usr.address,
		"availability" : usr.availability
	}

	return render(request, "mprofile.html", context)

# def image(request):
# 	data = request.POST
# 	form = MaidSignUp.objects.get(username = data['usrname'])
# 	form.imagename = data['usrname']+data['password']
# 	form.save()
# 	myfile = request.FILES['myfile']
# 	fs = FileSystemStorage()
# 	filename = fs.save(form.imagename, myfile)
# 	form.uploaded_file_url = fs.url(filename)
# 	form.save()

# 	return render(request, 'core/maid registration.html')
       
	# data =
	# file = open(path,'w')
	# file.write(request.POST['image'])
	# file.close()

def delete(request):

	return render(request, 'homepages.html')

