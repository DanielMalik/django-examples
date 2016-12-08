from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from mysql.connector import connect


@csrf_exempt
def add_game(request):
    query = "SELECT id, name FROM Teams;"

    try:
        cnx = connect(user='root', password='dupa', host='localhost', database='projekt_1')
        cursor = cnx.cursor()
        cursor.execute(query)
    except:
        raise

    select1 = ''

    for row in cursor:
        select1 += "<option value=%s>%s</option>" % row

    answer = """
        <html>
            <body>
                <form action="/add_game" method="POST">
                    <label>Host 
                        <select name="host_id">
                            %s
                        </select>
                    </label>
                    <label> Guest 
                        <select name="guest_id">
                            %s
                        </select>
                    </label>
                    <input type="number" name="host_goals" value="0">
                    <input type="number" name="guest_goals" value="0">
                    <input type="submit" name="addGame" value="Zapisz">
                </form>
            </body>
        </html>""" % (select1, select1)


    if request.method == "POST":
        host_id = request.POST.get("host_id")
        guest_id = request.POST.get("guest_id")

        host_goals = request.POST.get("host_goals")
        guest_goals = request.POST.get("guest_goals")

        host_goals = int(host_goals)
        guest_goals = int(guest_goals)

        if host_goals < 0 or guest_goals < 0:
            return HttpResponse(answer + "wyniki sa ujemne")

        insert = """INSERT INTO Games 
            (id, team_home, team_away, team_home_goals, team_away_goals) 
            VALUES (0, %s, %s, %s, %s);
            """ % (host_id, guest_id, host_goals, guest_goals) 

        print(insert)

        cursor.execute(insert)
        cnx.commit()

        cursor.close()
        cnx.close()
        return HttpResponseRedirect("/games?id=%s" % host_id)

    return HttpResponse(answer)



@csrf_exempt
def tempConverter(request):
    form = """
        <form action="#" method="POST">
            <label>
                Temperatura:
                <input type="number" min="0.00" step="0.01" name="degrees" value=%s>
            </label>
            <input type="submit" name="convertionType" value="CelcToFahr">
            <input type="submit" name="convertionType" value="FahrToCelc">
        </form>

    """

    if request.method == "POST":
        temp = request.POST.get("degrees")
        temp = float(temp)
        convertionType = request.POST.get("convertionType")

        if convertionType == "CelcToFahr":
            new_temp = 32 + 9/5 * temp
        else:
            new_temp = 5/9 * (temp - 32)

        new_temp = "%.2f" % new_temp
        return HttpResponse(form % new_temp)


    return HttpResponse(form % "")
