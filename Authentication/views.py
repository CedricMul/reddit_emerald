from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views import View
from Authentication.forms import LoginForm, RegisterForm
from User.models import RedditUser


class loginView(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        if not request.user.is_authenticated:
            registration = 'Create an account'
        return render(request, "generic_form.html", {"form": form, "registration": registration})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
            else:
                return render(request, "user_not_found.html")


class registerView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = RedditUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))


class logoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("homepage"))
