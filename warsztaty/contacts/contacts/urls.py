from django.conf.urls import url
from django.contrib import admin

from contact_book.views import NewContact, ModifyContact, DeleteContact, ShowContact, ShowContactList

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^new$', NewContact.as_view()),
    url(r'^modify/(?P<contact_id>(\d)+)$', ModifyContact.as_view()),
    url(r'^delete/(?P<contact_id>(\d)+)$', DeleteContact.as_view()),
    url(r'^show/(?P<contact_id>(\d)+)$', ShowContact.as_view()),
    url(r'^$', ShowContactList.as_view()),

]
