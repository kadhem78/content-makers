from django.db import models
from accounts.models import User
# Create your models here.
from .utils import unique_slug_generator
class Categorie(models.Model):
	creator = models.ForeignKey(User , on_delete = models.CASCADE)
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=70 , null=True , blank=True)
	created_at = models.DateTimeField(auto_now=True)
	update_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def save(self , *args , **kwargs):
		self.slug = unique_slug_generator(self)
		super(Categorie , self).save(*args , **kwargs)


def imageupload(instance, filename):
    image_name , extention = filename.split('.')
    return 'courses/{0}/images/{1}.{2}'.format(instance.title, instance.title , extention)




class Course(models.Model):
	LEVELS = [
    ('Beginner', 'Beginner'),
    ('Advanced', 'Advanced'),
    ('Profissional', 'Profissional'),
    ]
	categorie = models.ForeignKey(Categorie , on_delete = models.CASCADE , related_name='courses' )
	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=70 , null=True , blank=True)
	course_img = models.ImageField(upload_to = imageupload ) 
	decription = models.TextField(default='')
	course_url = models.URLField(max_length = 200)
	level = models.CharField(max_length=70, choices=LEVELS, default='Beginner')
	created_at = models.DateTimeField(auto_now=True)
	update_at = models.DateTimeField(auto_now_add=True)
 
	def __str__(self):
		return self.title

	def save(self , *args , **kwargs):
		self.slug = unique_slug_generator(self)
		super(Course , self).save(*args , **kwargs)


def certificateupload(instance, filename):
    image_name , extention = filename.split('.')
    return 'certificates/{0}/images/{1}.{2}'.format(instance.owner, instance.owner , extention)






