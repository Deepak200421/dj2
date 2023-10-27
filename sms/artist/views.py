import json

from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.mail import send_mail
import random
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Persons
from django.views.generic import ListView


# Create your views here.
def myworks(request):
    mw = [
        {'category': 'Absract Painting',
         'doc': '30-08-2023',
         'price': '1000 USD',
         'rating': '5',
         'inspiration': 'From Nature',
         },

        {'category': 'Digital',
         'doc': '15-07-2023',
         'price': '500 USD',
         'rating': '4',
         'inspiration': 'Technology',
         }
    ]
    return render(request, 'artist/myworks.html', {'mw': mw})


# return render(request, 'artist/myworks.html')

def hanees(request):
    return render(request, 'artist/hanees.html')


def history(request):
    works = [
        {"noc": "M",
         "pd": "30-09-2022",
         "mop": "Cash",
         "amount": "1000 USD",
         "ac": "Abstract Painting",
         },

        {"noc": "Deepak",
         "pd": "31-8-2022",
         "mop": "UPI",
         "amount": "5000 USD",
         "ac": "Digital Painting",
        },
    ]


    return render(request, 'artist/history.html',{'works':works})




def climate(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'True')

        resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=52839ba9ecd4168ea6254a065b69ae27')
        data = resp.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        context = {
            'city': city,
            "country_code": str(data['sys']['country']),
            "longitude": str(data['coord']['lon']),
            "latitude":str(data['coord']['lat']),
            "temp": str(round(temp_celsius, 2)) + '°C',
            "pressure": str(data['main']['pressure']),
            "humidity": str(data['main']['humidity']),
        }
    else:
        context = {}
    return render(request, 'artist/climate.html',context)


def home(request):
    return render(request, 'artist/base.html', {'title': 'Home'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('artist-base')
    else:
        form = UserRegisterForm()
    return render(request, 'artist/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'artist/profile.html')









otp_storage = {}

def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()
        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'artist/validate_otp.html')
    return render(request, 'artist/send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_otp = request.POST['otp']

        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:
            return redirect('login')
        else:
            return render(request, 'artist/validate_otp.html', {'msg': 'Invalid OTP'})

    return render(request, 'artist/validate_otp.html')




class ContactListView(ListView):
    paginate_by = 4
    model = Persons
def list_persons(request):
    person_list = Persons.objects.all()
    paginator = Paginator(person_list,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'artist/list_persons.html', {"page_obj": page_obj})




import razorpay
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .constants import PaymentStatus
from .models import Order as o

import json

def home(request):
    return render(request, "artist/index.html")

def order_payment(request):
    if request.method == "POST":
        # Extract data from the POST request
        name = request.POST.get("name")
        amount = request.POST.get("amount")

        # Create a Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create a Razorpay order
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )

        # Create an Order object and save it in the database
        order = o.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()

        # Render the payment template with the order information
        return render(
            request,
            "artist/payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )

    return render(request, "artist/payment.html")


@csrf_exempt
def callback(request):
    # Define a function to verify the payment signature
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        result = client.utility.verify_payment_signature(response_data)
        if result:
            return True
        else:
            return False

    # Check if a Razorpay signature is present in the POST data
    if "razorpay_signature" in request.POST:
        # Extract data from the POST request
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = o.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()

        # Verify the payment signature
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "artist/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "artist/callback.html", context={"status": order.status})
    else:

        payment_id = request.POST.get("error[metadata]")
        if payment_id:
            payment_id = json.loads(payment_id).get("payment_id")

        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = o.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "artist/callback.html", context={"status": order.status})
