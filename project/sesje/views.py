from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

COUNTER = 'counter'
LOGGED_USER = 'loggedUser'


class Login(View):

    def get(self, request):
        if LOGGED_USER in request.session:
            loggedUser = request.session.get(LOGGED_USER)
            ctx = {'name' : loggedUser}
            return render(request, "hello.html", ctx)
        else:
            return render(request, "login_form.html")


    def post(self, request):
        action = request.POST.get("login")
        if action == "login":
            user_name = request.POST.get("name")
            request.session[LOGGED_USER] = user_name
            ctx = {'name' : user_name}
            return render(request, "hello.html", ctx)

        elif action == "logout":
            if LOGGED_USER in request.session:
                del(request.session[LOGGED_USER])
            return render(request, "login_form.html")



class SetSession(View):

    def get(self, request):
        request.session[COUNTER] = 0
        return HttpResponse("Counter wyzerowany")


class ShowSession(View):

    def get(self, request):
        print(request.session.get(COUNTER))
        if COUNTER in request.session:
            counter = request.session.get(COUNTER)
            counter = int(counter)
            counter += 1
            request.session[COUNTER] = counter
            return HttpResponse("Counter = %s"%counter)
        else:
            return HttpResponse("Counter nie istnieje")

class DeleteSession(View):

    def get(self, request):
        if COUNTER in request.session:
            del(request.session[COUNTER])
            return HttpResponse("Counter usunięty")
        else:
            return HttpResponse("Counter nie istanie")
