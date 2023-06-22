from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from authentication.serializers import UserSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = UserSerializer
    
    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="get",
    )
    def get_user(self, request):
        user = request.user
        carts = Cart.objects.filter(user__email=user)
        items = []
        for cart in carts:
            item = cart.item
            items.append(
            {
                "id": cart.pk,
                "name": str(item.name),
                #"description": str(item.description),
                "cost": int(item.cost),
                "amount": str(cart.amount),
                "image_url": 'http://127.0.0.1:8000' + str(item.image.url).removeprefix('/images')
            })
        return Response({"items": items})