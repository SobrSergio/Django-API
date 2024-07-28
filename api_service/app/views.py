from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Ad
from .serializers import AdSerializer, UserSerializer

class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        id = self.kwargs.get('id')
        
        # Проверяем, находится ли id в допустимом диапазоне
        try:
            id = int(id)
            if not (1 <= id <= 10):
                raise ValueError("ID должен быть в диапазоне от 1 до 10")
        except ValueError as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Находим объект по id
        try:
            return Ad.objects.get(id=id)
        except Ad.DoesNotExist:
            return Response({
                'error': 'Объявление не найдено'
            }, status=status.HTTP_404_NOT_FOUND)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

# Обработка ошибки токена
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthenticationFailed(AuthenticationFailed):
    def __init__(self, detail):
        super().__init__(detail=detail)

def custom_exception_handler(exc, context):
    if isinstance(exc, CustomAuthenticationFailed):
        return Response({
            'detail': 'Токен не действителен или истек'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    return None
