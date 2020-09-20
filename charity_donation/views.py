# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category, Institution, Donation
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LandingPage(View):
    def get(self, request):
        quantity = Donation.objects.all()
        bags_number = 0
        for n in quantity:
            bags_number = bags_number + n.quantity
            return bags_number

        institution_number = 0
        for n in quantity:
            institution_number = institution_number + n.institution
            return institution_number
        fundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        local_founds = Institution.objects.filter(type=3)
        ctx = {
            'bags_number': bags_number,
            'institution_number': institution_number,
            'fundations': fundations,
            'ngos': ngos,
            'local_founds': local_founds}

        return render(request, "charity_donation/index.html", ctx)

class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        cat = Category.objects.all()
        institutions = Institution.objects.all()

        ctx = {
            'cat': cat,
            'institutions': institutions }
        return render(request, "charity_donation/form.html", ctx)

    def post(self, request):
        quantity = request.POST.get('bags')
        categories = request.POST.getlist('categories')
        institution = Institution.objects.get(name=request.POST.get('organization'))
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        user = User.objects.get(email=request.user.email)

        new_donation = Donation.objects.create(quantity=quantity, institution=institution, address=address,
                                               phone_number=phone_number, city=city, zip_code=zip_code,
                                               pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment, user=user)
        for category in categories:
            new_donation.categories.add(Category.objects.get(name=category))
        new_donation.save()

        return redirect(reverse('form-confirmation'))


class Login(View):
    def get(self, request):
        return render(request, "charity_donation/login.html")

    def post(self, request):

        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main'))
        else:
            return render(request, "charity_donation/register.html")

class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main'))



class Register(View):
    def get(self, request):
        return render(request, "charity_donation/register.html")

    def post(self, request):
        email = request.POST['email']
        username = request.POST['email']
        first_name = request.POST['name']
        last_name = request.POST['surname']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(email = email, username=username, first_name = first_name, last_name = last_name, password=password)
            user.save();
            return render(request, "charity_donation/login.html")
        else:
            return render(request, "charity_donation/register.html")


class InstitutionCreate(CreateView):
  model = Institution
  fields = '__all__'
  success_url = reverse_lazy("charity_donation/index.html")

class CategoryCreate(CreateView):
      model = Category
      fields = '__all__'
      success_url = reverse_lazy("charity_donation/index.html")



class UserPage(View):
    def get(self, request):
        return render(request, "charity_donation/profil.html")

class FormConfirmation(View):

    def get(self, request):
        return render(request, 'charity_donation/form-confirmation.html')