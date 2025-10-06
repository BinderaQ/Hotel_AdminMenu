from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomSignUpForm
urlpatterns = [
    path('',views.room_list, name='room_list'),
    path('testing/create/', views.create_booking,name = 'create_booking'),
    path('show/', views.show_calendar, name = 'show_calendar'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('testing/<int:booking_id>/cancel',views.cancel, name = 'cancel'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup, name='signup'),
    path("success/", views.success, name="success"),
]