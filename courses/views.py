from django.shortcuts import render , redirect
from django.urls import reverse
from .forms  import CourseForm , SearchForm
from .models import Course , Categorie
from accounts.models import Student , User
from accounts.forms import StudentCreation , StudentSignUpForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import student_required , teacher_required , login_check

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView


@login_required
@teacher_required
def manage(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'courses' : page_obj
    }
    return render(request , 'manage/manage.html' , context)

@login_required
@teacher_required
def create_course(request):
    if request.method == 'POST' :
        form = CourseForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage'))
    else:
        form = CourseForm()
    context = {
    'form' : form
    }
    return render(request , 'manage/createcourse.html' , context)

@login_required
@teacher_required
def update_course(request , slug):
    course = Course.objects.get(slug = slug)
    if request.method == 'POST':
        form = CourseForm(request.POST , request.FILES , instance=course)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect(reverse('manage'))
    else:
        form = CourseForm(instance=course)
    context = {
    'form' : form
    }
    return render(request , 'manage/updatecourse.html' , context)


@login_required
@teacher_required
def delete_course(request , slug):
    Course.objects.get(slug = slug).delete()
    return redirect(reverse('manage'))




@login_required
@student_required
def userprofile(request):
    categories  = Categorie.objects.all()
    student = Student.objects.get(user = request.user)
    context = {
    'student' : student , 
    'categories': categories , 
    }
    return render(request , 'profile.html' , context)

@login_required
@student_required
def courses(request , slug): 
    categories = Categorie.objects.all()
    categorie = Categorie.objects.get(slug = slug)
    student = Student.objects.get(user = request.user )
    courses = categorie.courses.filter(level = student.level)
    paginator = Paginator(courses, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'courses': page_obj,
    'categories' : categories,
    }
    return render(request , 'student_course.html' , context)

@login_required
@teacher_required
def students(request):
    searchform = SearchForm()
    users = User.objects.filter(location = request.user.location)
    paginator = Paginator(users, 21)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'users' : page_obj,
    'searchform' : searchform
    }
    return render(request , 'manage/students.html' , context)

@login_required
@teacher_required
def updatestudent(request , username):
    user = User.objects.get(username = username)
    student = Student.objects.get(user = user)
    if request.method == 'POST':
        form = StudentCreation(request.POST , instance=student)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect(reverse('students'))
    else:
        form = StudentCreation(instance=student)
    context = {
    'form' : form , 
    'student' : student
    }
    return render(request , 'manage/updatestudent.html' , context)

"""def render_pdf_view(request , username):
    user = User.objects.get(username = username)
    student = Student.objects.get(user = user)
    template_path = 'user_card.html'
    context = {'student': student}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response"""



""" dirhem kole fi view wa7da ab3ethlaha fi l url title ta3 kole categorie w hiy dire filtrage w rage3 lnafesse lpage """
@login_required
@teacher_required
def search(request):
    if request.method == 'GET' : 
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            searchkey = searchform.cleaned_data['keyword']
            searchresult = Student.objects.filter(
                Q(level__icontains = searchkey) |
                Q(domain__icontains = searchkey) |
                Q(user__username__icontains = searchkey)
            )
            context = {
            'searchform' : searchform , 
            'searchkey' : searchkey , 
            'searchresult': searchresult
            }
            return render(request , 'manage/students.html' , context)
        else:
            return redirect('/manage/students')
    else:
        return redirect('/manage/students')








