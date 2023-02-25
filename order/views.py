from django.http import JsonResponse
from django.shortcuts import render

from order.models import Shop
from order.serializer import ShopSerializer


def shop(request):
    if request.method == 'GET':
        # snippets = Snippet.objects.all()    # Snippet 은 데이터 베이스 이름이다
        # serializer = SnippetSerializer(snippets, many=True)
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':

# Create your views here.
