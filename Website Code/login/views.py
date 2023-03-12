from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from ShareAndCare import views

email = ''
password = ''
msg = ''


# Create your views here.
def loginaction(request):
    data = {
        "title" : "Share & Care | Login",
        "css" : "/static/css/login.css",
        "customCSS" : "",
    }
    
    global email, password, msg
    try:
        if request.method == "POST":
            # Connection with the Database
            m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>")  
            cursor = m.cursor()

            email = request.POST['email']
            password = request.POST['password']

            c = "select * from users where Email='{}' and Password='{}'".format(email, password)
            print(c)
            cursor.execute(c)
            t = tuple(cursor.fetchall())
            print(t)
            
            if len(t) == 0:
                data = {
                    "title" : "Share & Care | Login",
                    "css" : "/static/css/login.css",
                    "customCSS" : "alert-danger",
                }

                print(len(t))
                messages.success(request, 'Invalid Details.')
                return render("login", data)
            else:
                msg = "Welcome, {} {}".format(t[0][0], t[0][1])
                messages.success(request, msg)
                return redirect("services")
    except:
        print("Exception")
        pass

    return render(request, "login.html", data)
