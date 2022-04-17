import django_filters
from accounts.models import Student


class StudentFilter(django_filters.FilterSet):
	class Meta:
		model = Student
		fields = ['user' , 'domain' , 'level']