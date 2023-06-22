from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from authentication.serializers import UserSerializer




class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = UserSerializer
    
    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="get",
    )
    def get_user(self, request):
        user = request.user
        orders = Order.objects.filter(user__email=user)
        items = []
        for order in orders:
            item = order.item
            items.append(
            {
                "id": order.pk,
                "name": str(item.name),
                #"description": str(item.description),
                "cost": str(item.cost),
                "amount": int(order.amount),
                "status": str(order.status),
                "image_url": 'http://127.0.0.1:8000' + str(item.image.url).removeprefix('/images')
            })
        return Response({"items": items})
