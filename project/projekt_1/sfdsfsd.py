def ship(request):
    ship = {
"type": "YT-1300 Light Freighter", "name": "Millenium Falcon", "owner": "Han Solo"
    }
    return render(request, "ship.html",
ship)
