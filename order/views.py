from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from order.models import Shop
from order.serializer import ShopSerializer


@csrf_exempt    # csrf = 보안적인, 프론트와 백에서 데이터를 바꿔치기를 방지한다
def shop(request):
    if request.method == 'GET':
        # snippets = Snippet.objects.all()    # Snippet 은 데이터 베이스 이름이다
        # serializer = SnippetSerializer(snippets, many=True)
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
