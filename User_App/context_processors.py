from User_App.models import Cart

def context(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user, ordered=False).count()
    else:
        cart_count = 0

    context = {
        'cart_count' : cart_count
    }
    return context