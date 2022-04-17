from django.urls import path
from . import views 

urlpatterns = [
    path('', views.manage , name='manage'),
    path('create_course/', views.create_course , name='create_course'),
    path('update/<slug:slug>/', views.update_course , name='update_course'),
    path('delete/<slug:slug>/', views.delete_course , name='delete_course'), 
    path('profile/', views.userprofile , name='userprofile'),
    path('courses/<slug:slug>', views.courses , name='courses'), 
    path('students/', views.students , name='students'),
    path('update/<str:username>', views.updatestudent , name='updatestudent'),
    path('search/' , views.search , name='search'),
]
