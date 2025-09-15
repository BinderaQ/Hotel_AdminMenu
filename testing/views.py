from django.shortcuts import render, redirect
from .forms import BookingForm, CustomSignUpForm, CustomLogInForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room_list')
    else:
        form = CustomSignUpForm()
    return render(request, 'testing/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLogInForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room_list')
    else:
        form = CustomLogInForm()
    return render(request, 'testing/login.html', {'form': form})


from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

#
from .models import Room,Booking

def room_list(request):
    rooms = Room.objects.all()
    return render(request, "testing/room_list.html",{'rooms':rooms})

def success(request):
    return render(request, "testing/success.html")

def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            send_mail(
                "Пітвердженя замовлення",
                f"Ви забронювали {booking.room.name} з {booking.start_date} по {booking.end_date}",
                "nouneim1939@gmail.com",
                [request.user.email],
                fail_silently=False,
            )
            return redirect("success")
    else:
        form = BookingForm()
    return render(request,"testing/booking_form.html", {"form":form})

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return render(request, 'testing/logout.html')

def show_calendar(request):
    rooms = Room.objects.all()
    today = date.today()
    dates = [today+ timedelta(days=x) for x in range(30)]
    free = {}
    for room in rooms:
        free[room] = []
        for d in dates:
            is_booked = Booking.objects.filter(room=room,start_date__lte = d,end_date__gte = d).exists()
            free[room].append((d,not is_booked))
    return render(request, 'testing/show_calendar.html',{'free':free, 'dates':dates})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render (request, 'testing/my_bookings.html', {'bookings':bookings})

@login_required
def cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect('my_bookings')
    return render (request,'testing/cancel.html', {'booking':booking})
