from django.urls import path

from . import views


urlpatterns = [
    # ex: /users/1,2
   # path('<int:request_id>/',views.join,name = 'join-ride'),
    path('<int:request_id>/', views.rideDetail, name='rideDetail'),
    path('<int:request_id>/edit_destination/', views.edit_destination, name='edit_destination'),
    path('<int:request_id>/edit_time/', views.edit_time, name='edit_time'),
    path('<int:request_id>/edit_num_passanger/', views.edit_num_passanger, name='edit_num_passanger')
]
