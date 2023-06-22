from authentication.models import User
from .serializers import UserSerializer

from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, reauest):
    #     users = User.objects.all()
    #     user_serialised = UserSerializer(users, )
    #     return Response(user_serialised.data)

    @action(methods=["POST"], detail=False, url_path="registration")
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"msg": "Registred successfully", "user": serializer.data})

    @action(methods=["POST"], detail=False, url_path="login")
    def login(self, request):
        if "email" not in request.data:
            raise ValidationError({"error": "no email"})
        if "password" not in request.data:
            raise ValidationError({"error": "no password"})

        try:
            user = User.objects.get(email=request.data["email"])
        except User.DoesNotExist:
            raise NotFound({"error": "пользователь не найден"})

        if not user.check_password(request.data["password"]):
            raise AuthenticationFailed({"error": "wrong password"})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie("refresh", str(refresh))
        response.data = {"access": str(refresh.access_token)}
        return response

    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="account",
    )
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)
    
    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="account",
    )
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="logout",
    )
    def logout(self, request):
        response = Response()
        response.delete_cookie("refresh")
        return response
