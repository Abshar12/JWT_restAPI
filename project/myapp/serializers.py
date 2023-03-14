from rest_framework import serializers
from myapp.models import Client,Merchant
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"
        
class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields  = "__all__"
        

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)