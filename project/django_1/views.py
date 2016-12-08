from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint

from mysql.connector import connect


def show_hello(request):
    name = "Ola"
    answer = """
        <html>
            <body>
                <p> Hello world! </p>
                <a href="/random?name=%s"> PRZEKIERUJ </a>
            </body>
        </html>
        """ % name
    return HttpResponse(answer) 

def show_hello_redirect(request):
    return HttpResponseRedirect("http://www.google.com")


def show_random(request):
    name = ""
    if request.method == "GET":
        name = request.GET.get("name")

    random_number = randint(0, 100)
    answer = """
        <html>
            <body>
                <p> Cześć %s </p>
                <p> Wylosowaliśmy: %s </p>
            </body>
        </html>
        """ % (name, random_number)
    return HttpResponse(answer)

def show_random_max(request, max_number):
    random_number = randint(0, int(max_number))
    answer = """    
        <html>
            <body>
                <p> Wylosowaliśmy: %s </p>
            </body>
        </html>
        """ % random_number
    return HttpResponse(answer)



def print_numbers(request):
    if request.method == "GET":
        start = request.GET.get("start")
        end = request.GET.get("end")
        
        if start and end:
            response = HttpResponse()
            response.write("<html><body><ul>")

            try:
                start = int(float(start))
                end = int(float(end))
            except ValueError:
                return HttpResponse("Jeden z parametrow nie jest liczba")

            if (start > end):
                return HttpResponse("Start wieksze od end")

            for i in range(start, end + 1):
                response.write("<li>%s</li>" % i)
    
            response.write("</ul></body></html>")
            return response
           
        else:
            return HttpResponse("Brakuje ktoregos z parametrow")

    else:
        return HttpResponse("Metoda nie GET!")

def multy(request):
    if request.method == "GET":
        w = request.GET.get("w")
        h = request.GET.get("h")
        if w and h:
            try:
                w = int(w)
                h = int(h)
            except ValueError:
                return HttpResponse("Jeden z parametrow nie jest liczba")
            response = HttpResponse()
            response.write("<html><body><table>")

            for i in range(1, h + 1):
                response.write("<tr>")
                for j in range(1, w + 1):
                    response.write("<td> %s </td>" % (i * j))    
                response.write("</tr>")
            response.write("</table></body></html>")
            return response
        else:
            return HttpResponse("Brakuje ktoregos z parametrow")
    else:
        return HttpResponse("Metoda nie GET!")




def show_teams(request):
    query = "SELECT * FROM Teams ORDER BY id;"

    username = "root"
    passwd = "dupa"
    hostname = "127.0.0.1"
    db_name = "projekt_1"

    try:
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cursor = cnx.cursor()
        cursor.execute(query)
        answer = "<html><body>"
        for row in cursor:
            answer += "<a href='/games?id=%s'> %s - %s </a><br>" % (row[0], row[0], row[1])
        answer += "</body></html>"
        cursor.close()
        cnx.close()
        return HttpResponse(answer)
    except:
        raise 


def games_played(request):
    my_fav = 4;

    if request.method == "GET":
        if request.GET.get("id"):
            try:
                my_fav = int(request.GET.get("id"))
            except ValueError:
                pass

    query = """SELECT t1.name, t2.name, g.team_home_goals, g.team_away_goals
                FROM Games g 
                    INNER JOIN Teams t1 ON g.team_home=t1.id
                    INNER JOIN Teams t2 ON g.team_away=t2.id
                WHERE g.team_home=%s OR g.team_away=%s;
             """ % (my_fav, my_fav)

    username = "root"   
    passwd = "dupa"
    hostname = "127.0.0.1"
    db_name = "projekt_1"
    
    try:
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cursor = cnx.cursor()
        cursor.execute(query)
        answer = "<html><body>"
        for row in cursor:
            answer += "<p> %s grał z %s  wynik: %s : %s </p>" % row
        answer += "</body></html>"
        cursor.close()
        cnx.close()
        return HttpResponse(answer)
    except:
        raise 
