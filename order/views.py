from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

from order.models import Shop, Menu, Order, OrderFood
from order.serializer import ShopSerializer, MenuSerializer, OrderSerializer


@csrf_exempt  # csrf = 보안적인, 프론트와 백에서 데이터를 바꿔치기를 방지한다
def shop(request):
    if request.method == 'GET':
        # snippets = Snippet.objects.all()    # Snippet 은 데이터 베이스 이름이다
        # serializer = SnippetSerializer(snippets, many=True)
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)  # many=True 데이터가 여러개 있어도 상관 안한다
        # return render(request, 'order/shop_list.html', {'shop_list': shop})   # 굳이 할 필요없음, 프론트 작업
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu(request):
    if request.method == 'GET':
        # snippets = Snippet.objects.all()    # Snippet 은 데이터 베이스 이름이다
        # serializer = SnippetSerializer(snippets, many=True)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)  # many=True 데이터가 여러개 있어도 상관 안한다
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu_from_shop(request, shop):
    if request.method == 'GET':
        menu = Menu.objects.filter(shop=shop)  # filter 는 여러개 행들을 가져올 수 있다
        serializer = MenuSerializer(menu, many=True)  # many=True 데이터가 여러개 있어도 상관 안한다
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        address = data.get('address')
        shop = data.get('shop')

        # shop = request.POST['shop']   // html 이 있을 경우
        # address = request.POST['address']
        # food_list = request.POST.getList()

        food_list = data.get('food_list')
        order_date = timezone.now()

        shop_item = Shop.objects.get(pk=int(shop))
        shop_item.order_set.create(address=address, order_date=order_date, shop=int(shop))  # 자동으로 저장

        order_item = Order.objects.get(pk=int(shop_item.order_set.latest('id').id))
        for food in food_list:
            order_item.orderfood_set.create(food_name=food)
        return HttpResponse(status=200)
    elif request.method == 'GET':
        order = Order.objects.all()

        # related = Order.objects.select_related('orderfood_set')
        # set__all = Order.objects.prefetch_related('orderitem_set').all()

        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False)

