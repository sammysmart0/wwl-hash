from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from hashuser.models import CustomUser
from .serializers import CustomUserSerializers
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


@api_view(["POST"])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = CustomUserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny])
def login_view(request):
    form = AuthenticationForm(data=request.data)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    