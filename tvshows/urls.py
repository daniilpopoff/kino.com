from django.urls import path
from .views import tvShowList, tvShowDetail

urlpatterns = [
    path('show_list/', tvShowList),
    path('show_detail/<int:id>/', tvShowDetail),
]