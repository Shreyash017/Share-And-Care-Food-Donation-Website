from django.shortcuts import render, redirect
import mysql.connector as sql
from django.core.mail import send_mail, EmailMultiAlternatives

name = ''
email = ''
contact = ''
choice = ''
quantity = ''
address = ''
city = ''
state = ''
pin = ''


# Create your views here.
def receiveraction(request):
    data = {
        "title": "Share & Care | Receiver",
        "css": "/static/css/receiver.css",
    }

    global name, email, contact, choice, quantity, address, city, state, pin
    try:
        if request.method == "POST":
            # Connection with the Database
            m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>") 
            cursor = m.cursor()

            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            choice = request.POST['choice']
            quantity = request.POST['quantity']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['zipcode']
            print(choice, type(choice))

            c = "insert into receiver Values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, email, contact, choice, quantity, address, city, state, pin)
            print(c)
            cursor.execute(c)
            m.commit()

            com = "select Name, Email, Expire, Address from donor where city = '{}' and choice = '{}' and quantity >= {}".format(city, choice, quantity)
            print(com)
            cursor.execute(com)

            t = tuple(cursor.fetchall())
            print(t)

            if len(t) == 0:
                subject = 'Eye On Social'
                from_email = '<email id>'
                msg = '<p>Sorry, for the inconvenience currently there is <u>no stock</u> for your request. <br> <b>Kindly check later</b>.'
                to = email

                msg = EmailMultiAlternatives(subject, msg, from_email, [to])
                msg.content_subtype = 'html'
                msg.send()
            else:
                subject = 'Eye On Social'
                from_email = '<email id>'
                msg = "Thank You, for reaching out to us. In response to your query on <b>Share & Care</b> for Type: <b>'{}'</b> Quantity: <b>{}</b>. <br> Following are the details that satisfy your needs:-<br><br> {}".format(choice, quantity, t)
                to = email

                msg = EmailMultiAlternatives(subject, msg, from_email, [to])
                msg.content_subtype = 'html'
                msg.send()

            return redirect("home")
    except:
        print("Exception")
        pass

    return render(request, "receiver.html", data)
