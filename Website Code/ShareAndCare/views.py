from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def home(request):
    data = {
        "title" : "Share & Care",
        "css" : "/static/css/style.css",
    }

    return render(request, "index.html", data)


def aboutUs(request):
    data = {
        "title" : "Share & Care | About Us",
        "css" : "/static/css/style_about.css",
    }

    return render(request, "about.html", data)


def services(request):
    data = {
        "title" : "Share & Care | Services",
        "css" : "/static/css/style_service.css",
        "js" : "/static/js/index.js",
    }

    return render(request, "service.html", data)


def contact(request):
    data = {
        "title" : "Share & Care | Contact Us",
        "css" : "/static/css/style_contact.css",
    }

    try:
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        phone = request.GET['phone']
        choice = request.GET['choice']
        msg = request.GET['msg']
        
        print(fname, lname, email, phone, choice, msg)
        url = "/"
        return redirect(url)
    except:
        print("Exception")
        pass

    return render(request, "contact.html", data)
