from django.contrib import admin


from .models import Categorie , Course


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie' , 'level')
    list_filter = ('categorie' , 'level' , 'created_at')
    search_fields = ('title',)

