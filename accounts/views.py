from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from store.models import Customer


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(
                user=user, name=user.username, email=user.email
            )
            customer.save()
            return redirect("login")
    else:
        form = forms.UserRegisterForm()
    return render(request, "accounts/register.html", context={"form": form})
