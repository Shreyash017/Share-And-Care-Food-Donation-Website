from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from ShareAndCare import views

fname = ''
lname = ''
email = ''
password = ''


# Create your views here.
def signupaction(request):
    data = {
        "title": "Share & Care | Register",
        "css": "/static/css/style_register.css",
    }

    global fname, lname, email, password
    try:
        if request.method == "POST":
            # Connection with the Database
            m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>") 
            cursor = m.cursor()

            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']

            com = "select * from users where First_Name = '{}'".format(fname)
            print(com)
            c = "insert into users Values('{}', '{}', '{}', '{}')".format(fname, lname, email, password)
            print(c)
            cursor.execute(com)
            t = tuple(cursor.fetchall())
            print(t)

            if len(t) == 0:
                cursor.execute(c)
                m.commit()

                msg = "Welcome, {} {}".format(fname, lname)
                messages.success(request, msg)
                return redirect("services")
            else:
                messages.success(request, 'You have already registered. Kindly Login')
                return redirect("login")
    except:
        print("Exception")
        pass

    return render(request, "register.html", data)
