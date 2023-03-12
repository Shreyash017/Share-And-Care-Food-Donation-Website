from django.shortcuts import render
import mysql.connector as sql


# Create your views here.
def leaderboard(request):
    # Connection with the Database
    m = sql.connect(host="<host-name>", user="<user-name>", passwd="<password>", database="<db name>")
    cursor = m.cursor()

    c = "SELECT Name, City, Quantity FROM donor WHERE Privacy = 'no' ORDER BY Quantity DESC;"
    cursor.execute(c)
    t = tuple(cursor.fetchall())
    print(t)

    fname = t[0][0]
    fcity = t[0][1]
    sname = t[1][0]
    scity = t[1][1]
    tname = t[2][0]
    tcity = t[2][1]

    data = {
        "title": "Share & Care | Leaderboard",
        "css": "/static/css/leaderboard.css",
        "content": t,
        "fname": fname,
        "sname": sname,
        "tname": tname,
        "fcity": fcity,
        "scity": scity,
        "tcity": tcity,
    }

    return render(request, "leaderboard.html", data)
