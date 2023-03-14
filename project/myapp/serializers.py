from rest_framework import serializers
from myapp.models import Client,Merchant

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"
        
class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields  = "__all__"