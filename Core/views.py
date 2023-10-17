from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from User_App.models import PlaceOrder

# Create your views here.

def index(request):
    return render(request, 'Core/index.html')

@csrf_exempt
def get_placeorder(request):
    placeorder_id = request.POST.get('placeorder_id')
    placeorder = PlaceOrder.objects.get(id=placeorder_id)

    placeorder = {
        'first_name' : placeorder.first_name,
        'last_name' : placeorder.last_name,
        'address' : placeorder.address,
        'city' : placeorder.city,
        'phone' : placeorder.phone,
        'postel_code' : placeorder.postel_code,
        'order_note' : placeorder.order_note,
    }

    return JsonResponse({'response':'address geted','placeorder':placeorder})