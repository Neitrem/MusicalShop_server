from rest_framework.views import APIView

from item.models import Item
from rest_framework.response import Response

from order.models import Order


class CartApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        items = Item.objects.all()
        items_cart = []
        name = ""
        for item in items:
            if item.cart:
                if str(item.cart.user) == pk:
                    name = item.cart.user.name
                    items_cart.append(item)
        if len(items_cart) > 0:
            items = []
            for item in items_cart:
                items.append({
                    "name": str(item.name),
                    "description": str(item.description),
                    "cost": str(item.cost),
                    "amount": str(item.amount)}
                )
            return Response({
                "user": {
                    "email": str(pk),
                    "name": str(name)
                },
                "items":items,
            })
        return Response({"data": "error"})


class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        items = Item.objects.all()
        orders = {}
        for item in items:
            if item.order:
                if str(item.order.user) == pk:
                    if item.order not in orders.keys():
                        orders[item.order.id] = {}
                        orders[item.order.id]["status"] = item.order.status
                        orders[item.order.id]["items"] = []
                    orders[item.order.id]["items"].append({
                        "name": str(item.name),
                        "description": str(item.description),
                        "cost": str(item.cost),
                        "amount": str(item.amount)
                    })
        if len(orders) > 0:
            return Response({
                "orders":orders,
            })
        return Response({"data": "error"})
