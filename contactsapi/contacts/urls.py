from django.urls import path
from .views import ContactList, ContactDetailView


urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('<int:id>', ContactDetailView.as_view(), name='detail_view')
]