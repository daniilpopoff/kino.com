from django.urls import path
from .views import CreatePersonView, PersonListView, PersonDetailView, DeletePersonView, UpdatePersonView

urlpatterns = [
    path('person_list/', PersonListView.as_view()),
    path('person_list/<int:id>/', PersonDetailView.as_view()),
    path('person_list/<int:id>/delete/', DeletePersonView.as_view()),
    path('person_list/<int:id>/update/', UpdatePersonView.as_view()),
    path('create_person/', CreatePersonView.as_view())
]
