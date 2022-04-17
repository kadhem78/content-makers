from django.db import models

# Create your models here.
class Testimonials(models.Model):
	name = models.CharField(max_length=25)
	position = models.CharField(max_length=25)
	content = models.TextField(default='')

	def __str__(self):
		return self.name

class Questions(models.Model):
	question = models.TextField(default='')
	response = models.TextField(default='')

	def __str__(self):
		return 'Question %s' % self.id
def imageupload(instance, filename):
    image_name , extention = filename.split('.')
    return 'Sponsors/{0}/images/{1}.{2}'.format(instance.name, instance.name , extention)

class Sponsor(models.Model):
	name = models.CharField(max_length=25)
	logo = models.ImageField(upload_to = imageupload )
	def __str__(self):
		return self.name



"""course_url = models.URLField(max_length = 200)"""

class Contact(models.Model):
	email = models.EmailField(max_length=200)
	phone = models.CharField(default='' , max_length=100)
	work_hours = models.CharField(default='' , max_length=100)
	address = models.TextField(max_length=250)
	facebook = models.URLField(max_length=300)
	instagram = models.URLField(max_length=300)

	def __str__(self):
		return "our_contact"
