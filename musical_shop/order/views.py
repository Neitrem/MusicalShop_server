from rest_framework import generics
from rest_framework.views import APIView

from order.models import Order
from order.serializers import OrderSerializer


class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        items = Order.objects.where(Order.user==pk)
        print(items)
