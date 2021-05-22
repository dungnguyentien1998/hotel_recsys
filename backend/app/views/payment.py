import json
from app import models
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        domain_url = 'http://localhost:8000/api/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            data = json.loads(request.body)
            booking_to_purchase = ''
            bookings = models.Booking.objects.all()
            for booking in bookings:
                if booking.uuid == data['booking_id']:
                    booking_to_purchase = booking

            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'canceled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': booking_to_purchase.code,
                        'quantity': 1,
                        'currency': 'VND',
                        'amount': booking_to_purchase.total_price,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

