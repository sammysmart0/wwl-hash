from rest_framework import serializers
from hashuser.models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = (
        'id',
        'username',
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'phone_number',
        'email',
        'matric_number',
        'department',
        'password',
      )