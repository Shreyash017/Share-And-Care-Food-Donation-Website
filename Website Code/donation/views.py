from django.shortcuts import render, redirect
import mysql.connector as sql

name = ''
email = ''
noc = ''
cn = ''
amt = ''


# Create your views here.
def paymentaction(request):
    data = {
        "title": "Share & Care | Donation",
        "css": "/static/css/payment.css",
    }

    global name, email, noc, cn, amt
    try:
        if request.method == "POST":
            # Connection with the Database
            m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>")
            cursor = m.cursor()

            name = request.POST['name']
            email = request.POST['email']
            noc = request.POST['noc']
            cn = request.POST['ccn']
            amt = request.POST['amt']

            c = "insert into donation Values('{}', '{}', '{}', {}, {})".format(name, email, noc, cn, amt)
            print(c)
            cursor.execute(c)
            m.commit()

            return redirect("home")
    except:
        print("Exception")
        pass

    return render(request, "payment.html", data)
