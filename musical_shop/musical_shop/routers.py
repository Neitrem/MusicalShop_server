from authentication.views import UserViewSet
from cart.views import CartViewSet
from order.views import OrderViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("carts", CartViewSet)
router.register("orders", OrderViewSet)
