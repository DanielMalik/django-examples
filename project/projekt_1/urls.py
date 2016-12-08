from django.conf.urls import url
from django.contrib import admin

from django_1.views import show_hello, show_random, show_teams, show_random_max, show_hello_redirect, print_numbers, multy, games_played
from forms.views import tempConverter,add_game

from sesje.views import SetSession, ShowSession, DeleteSession, Login
from football.views import ShowStats, Hej, ShowTeams


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', show_hello),
    url(r'^hello2$', show_hello_redirect),

    url(r'^random$', show_random),

    url(r'^random/(?P<max_number>(\d)+)$', show_random_max),

    url(r'^teams$', ShowTeams.as_view()),

    url(r'^print$', print_numbers),
    url(r'^multy$', multy),
    url(r'^games$', games_played),
    url(r'^temp$', tempConverter),
    url(r'^add_game$', add_game),

    url(r'^set_counter$', SetSession.as_view()),
    url(r'^show_counter$', ShowSession.as_view()),
    url(r'^delete_counter$', DeleteSession.as_view()),

    url(r'^stats/(?P<team_id>(\d)+)$', ShowStats.as_view()),

    url(r'^hej$', Hej.as_view()),
    url(r'^login$', Login.as_view())
]
