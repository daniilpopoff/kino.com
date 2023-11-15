from django.urls import path
from .views import create_person, person_list, delete_person, update_person

urlpatterns = [
    path('person_list/', person_list),
    path('person_list/<int:id>/delete/', delete_person),
    path('person_list/<int:id>/update/', update_person),
    path('create_person/', create_person)
]