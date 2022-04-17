from django.contrib import admin
from .models import Location , User , Student , SignupSwitch

from .forms import UserFormAdmin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdminUserCreation(UserAdmin):
	model= User
	add_form = UserFormAdmin
	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'user role',
			{

				'fields':(

					'is_student',
					'is_organizer',
					'location',
					)


			}
			)

		)

admin.site.register(Location)
admin.site.register(User , AdminUserCreation)
admin.site.register(SignupSwitch)

@admin.register(Student)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    list_filter = ('level',)
