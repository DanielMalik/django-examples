from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from contact_book.models import Contact
from mysql.connector import connect


class NewContact(View):

    def get(self, request):
        return render(request, "new_contact.html")

    def post(self, request):
        new_contact_name = request.POST.get("contact_name")
        new_contact_surname = request.POST.get("contact_surname")
        new_contact_mail = request.POST.get("contact_mail")
        new_contact_phone_number = request.POST.get("contact_phone_number")

        query = """
            INSERT INTO Contacts (id, name, surname, mail, phone_number)
                VALUES (0, '%s', '%s', '%s', '%s');
                """ % (new_contact_name, new_contact_surname, new_contact_mail, new_contact_phone_number)

        print(query)
        try:
            cnx = connect(user="root", password="dupa", host="127.0.0.1", database="contacts")
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
        except:
            raise 

        cursor.close()
        cnx.close()

        return HttpResponseRedirect("/")



class ModifyContact(View):

    def get(self, request, contact_id):
        return HttpResponse("ModifyContact")


class DeleteContact(View):

    def get(self, request, contact_id):
        return HttpResponse("DeleteContact")


# TODO: show info contact does not exist
class ShowContact(View):

    def get(self, request, contact_id):
        query = """SELECT id, name, surname, mail, phone_number 
                FROM Contacts WHERE id=%s;
                """ % contact_id

        try:
            cnx = connect(user="root", password="dupa", host="127.0.0.1", database="contacts")
            cursor = cnx.cursor()
            cursor.execute(query)
        except:
            raise 
        
        contact_from_cursor = cursor.fetchone()
        contact = Contact(
            contact_from_cursor[0],
            contact_from_cursor[1],
            contact_from_cursor[2],
            contact_from_cursor[3],
            contact_from_cursor[4])

        cursor.close()
        cnx.close()

        ctx = { 'contact' : contact}
        return render(request, "show_contact.html", ctx)


class ShowContactList(View):

    def get(self, request):
        query = """SELECT id, name, surname, mail, phone_number 
                FROM Contacts;"""

        try:
            cnx = connect(user="root", password="dupa", host="127.0.0.1", database="contacts")
            cursor = cnx.cursor()
            cursor.execute(query)
        except:
            raise 

        contacts = []
        for row in cursor:
            contact = Contact(row[0],row[1],row[2],row[3],row[4])
            contacts.append(contact)

        ctx = { 'contact_list' : contacts}

        return render(request, "contact_list.html", ctx)



