from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from mysql.connector import connect

class Hej(View):
    def get(self, request):
        ctx = {'name' : 'Ala'}
        return render(request, "hej.html", ctx)

class ShowStats(View):

    def get(self, request, team_id):

        query = """SELECT team_home, team_away, team_home_goals, team_away_goals 
            FROM Games 
            WHERE team_home=%s OR team_away=%s;
            """ % (team_id, team_id)

        query_name = """SELECT name FROM Teams WHERE id=%s;
            """ % team_id

        try:
            cnx = connect(user='root', password='dupa', host='localhost', database='projekt_1')
            cursor = cnx.cursor()
            cursor.execute(query)
        except:
            raise

        team_id = int(team_id)
        games_at_home = 0
        games_away = 0
        goals_scored = 0
        goals_lost = 0

        for row in cursor:
            team_home = row[0]
            team_away = row[1]
            goals_home = row[2]
            goals_away = row[3]

            if team_id == team_home:
                games_at_home += 1
                goals_scored += goals_home
                goals_lost += goals_away
            elif team_id == team_away:
                games_away += 1
                goals_scored += goals_away
                goals_lost += goals_home


        try:
            cursor.execute(query_name)
        except:
            raise

        team_name = cursor.fetchone()[0]
        


        answer = """ 
            <html>
                <body>
                    <h1>%s</h1>
                    Mecze w domu: %s <br>
                    Mecze wyjazdowe: %s <br>
                    Gole zdobyte: %s <br>
                    Gole stracone: %s <br>
                </body>
            </html>
            """ % (team_name, games_at_home, games_away, goals_scored, goals_lost)

        cursor.close()
        cnx.close()

        return HttpResponse(answer)

class ShowTeams(View):
    def get(self, request):
        query = "SELECT id, name FROM Teams ORDER BY id;"

        try:
            cnx = connect(user="root", password="dupa", host="127.0.0.1", database="projekt_1")
            cursor = cnx.cursor()
            cursor.execute(query)
        except:
            raise 
        
        teams_from_cursor = cursor.fetchall()

        cursor.close()
        cnx.close()
        ctx = {
            'title': 'Lista zespołów', 
            'teams' : teams_from_cursor
            }
        return render(request, "show_teams.html", ctx)


