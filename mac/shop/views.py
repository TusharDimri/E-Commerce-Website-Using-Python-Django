from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, Order_Update
from math import ceil
import json

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil( (n/4)-(n//4) )

    # params = { 'products': products, 'number_of_slides': nSlides, 'range' : range(1, nSlides) }

    # We will send a list of list to the template which contains different sliders
    # One list element of that list represents one slider of one category



    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides) ,nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html',  params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save() # Saves the data in the Database
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the Product Using the id
    product = Product.objects.filter(id=myid) # When no primary key is defined, django automatically creates
    #  a primary key with name 'id'

    return render(request, 'shop/prodView.html', {'product':product[0]} )

def checkout(request):
    if request.method == "POST":
        items_Json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(name=name, email=email, phone=phone,address=address,
                      city=city, zip_code=zip_code, state=state, items_json=items_Json)
        order.save()
        update = Order_Update(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = Order_Update.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse("{}")

    return render(request, 'shop/tracker.html')