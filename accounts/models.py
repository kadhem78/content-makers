from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class Location(models.Model):
	title = models.CharField(max_length=70 , unique=True)

	def __str__(self):
		return self.title



class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_organizer = models.BooleanField(default=False)
	location = models.ForeignKey(Location , on_delete = models.CASCADE , null=True)


def imageupload(instance, filename):
	image_name , extention = filename.split('.')
	return 'students/{0}/{1}.{2}'.format(instance.user, instance.user , extention)


class Student(models.Model):
	LEVELS = [
    ('Beginner', 'Beginner'),
    ('Advanced', 'Advanced'),
    ('Profissional', 'Profissional'),
    ]
	user = models.OneToOneField(User , on_delete=models.CASCADE)
	domain = models.CharField(max_length=70 , null=True)
	level = models.CharField(max_length=70 , choices=LEVELS, default='Beginner')
	profile_image = models.ImageField(upload_to = imageupload , null=True)
	def __str__(self):
		return self.user.username

class SignupSwitch(models.Model):
	switch_type = models.CharField(max_length=70 , default= 'main')
	on = models.BooleanField(default=True)
	def __str__(self):
		return 'signupswitch'