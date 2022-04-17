from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import StudentSignUpForm
from .models import User
from django.contrib.auth import authenticate , login , logout
from courses.decorators import login_check , switch_on
from django.utils.decorators import method_decorator



@method_decorator(login_check, name='dispatch')
@method_decorator(switch_on, name='dispatch')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/manage/profile')




def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/manage/profile')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				if user.is_student == True:
					return redirect('/manage/profile')
				else:
					return redirect('/manage')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('/')

