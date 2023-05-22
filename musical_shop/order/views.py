from rest_framework import generics
from rest_framework.views import APIView

from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.response import Response


class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        items = Order.objects.all()
        for item in items:
            if str(item.user) == pk:
                return Response({
                    "user": {
                        "email": str(item.user),
                        "name": str(item.user.name)
                    },
                    "item":{
                        "name": str(item.item.name),
                        "description": str(item.item.description),
                        "cost": str(item.item.cost),
                    },
                    "status": str(item.status)
                })
        return Response({"data": "error"})
