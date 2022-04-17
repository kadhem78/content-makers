from django.shortcuts import render , redirect
from courses.models import Categorie
# Create your views here.
from django.core.mail import send_mail

def home(request):
	categories = Categorie.objects.all()
	context = {
	'categories' : categories
	}
	return render(request , 'home.html' , context)


def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		send_mail= (

			name + subject,
			message , 
			email ,
			['kadhem.grib@gmail.com']

			)
		return redirect('/')


