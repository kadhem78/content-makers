from django.contrib import admin

# Register your models here.


from .models import Questions , Sponsor , Testimonials


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass
