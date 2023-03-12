from django.shortcuts import render, redirect
import mysql.connector as sql

name = ''
email = ''
contact = ''
choice = ''
type_of_food = ''
expire = ''
quantity = ''
address = ''
city = ''
state = ''
pin = ''
privacy = ''
future = ''


# Create your views here.
def donoraction(request):
    data = {
        "title" : "Share & Care | Donor",
        "css" : "/static/css/donor.css",
    }

    global name, email, contact, choice, type_of_food, expire, quantity, address, city, state, pin, privacy, future
    try:
        if request.method == "POST":
            print("Yes")
            # Connection with the Database
            m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>")  
            cursor = m.cursor()

            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            choice = request.POST['choice']
            type_of_food = request.POST['type']
            expire = request.POST['expire']
            quantity = request.POST['quantity']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['zipcode']
            privacy = request.POST['privacy']
            future = request.POST['future']
            print(choice, type(choice))

            c = "insert into donor Values('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}')".format(name, email, contact, choice, type_of_food, expire, quantity, address, city, state, pin, privacy, future)
            print(c)
            cursor.execute(c)
            m.commit()
            
            return redirect("home")
    except:
        print("Exception")
        pass

    return render(request, "donor.html", data)
