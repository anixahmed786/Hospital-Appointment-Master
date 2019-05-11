from django.http import HttpResponse
from django.shortcuts import render

from app.models import Appoinment,Contact_doc


def index(request):
    return render(request, 'app/index.html')


def services(request):
    return render(request, 'app/services.html')


def news(request):
    return render(request, 'app/news.html')


def detail(request):
    return render(request, 'app/detail.html')


def elements(request):
    return render(request, 'app/elements.html')


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


def base(request):
    return render(request, 'app/base.html')


def test(request):
    return render(request, 'app/test.html')


def appoinment(request):
    print("Sucessfully added...........")
    dept = request.POST["dept"]
    doctor = request.POST["doctor"]
    name = request.POST["name"]
    number = request.POST["number"]

    info = Appoinment(dept=dept, doctor=doctor, name=name, number=number)

    info.save()
    return render(request,"app/index.html")


def contact_doc(request):
    print("Sucessfully added...........")
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]

    info_doc = Contact_doc(name=name, email=email, subject=subject, message=message)

    info_doc.save()
    return render(request,"app/contact.html")
