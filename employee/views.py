from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings

def register_request(request):
	# if not request.user.is_authenticated:
	# 	return render(request=request, template_name="login.html", context={"login_form":form})

	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponse("Registration successful. Please contact admin for account activation.")
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return HttpResponse("Unsuccessful registration. Invalid information or password policy breach! / Username not available.")

	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			print(user)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/portal")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			return HttpResponse("Invalid login details supplied.")
			messages.error(request,"Invalid username or password.")

	if request.user.is_authenticated:
		return redirect("/portal")

	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required(login_url='/portal/login')
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/portal/login")

@login_required(login_url='/portal/login')
def homepage(request):
    items = Leads.objects.all()
    context = {
        'items': items,
        'header': 'Leads',
    }
    return render(request, 'home.html', context)

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain': request.META['HTTP_HOST'],
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/portal/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


def search_lead(request):
	query = request.GET.get("q")
	items = Leads.objects.filter(
		Q(company_name__icontains=query) | Q(contact_name__icontains=query) | Q(emails__icontains=query)
	)
	context = {
        'items': items,
        'header': 'Leads',
    }
	return render(request, 'home.html', context)