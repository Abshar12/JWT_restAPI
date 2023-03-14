from django.shortcuts import render
from rest_framework import status , serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from myapp.models import Client,Merchant
from myapp.serializers import ClientSerializer,MerchantSerializer
from django.contrib.auth import get_user_model
# Create your views here.




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        
        if Client.objects.filter(email=request.data['email']).exists():
            return Response("User already exists",status=status.HTTP_200_OK)
        
        merchant_serializer = MerchantSerializer(data=request.data)
        
        
        if merchant_serializer.is_valid():
            merchant_serializer.save()
            merchant_id=merchant_serializer.data['id']
            merchant  = Merchant.objects.get(id=merchant_id)
            client_data = request.data
            client_data["merchant"] = merchant.id
            client_serializer = ClientSerializer(data=client_data)
            
            if client_serializer.is_valid():
                print ('babu',client_serializer)
                client_serializer.save()
                
                return Response("User created successfully.",status=status.HTTP_201_CREATED)
        
        return Response("Some error occured.",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        permission_classes = [IsAuthenticated]
        user = Client.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        if Client.objects.filter(id=id).exists():
            user = Client.objects.get(pk=id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Details updated successfully",status=status.HTTP_200_OK)
        return Response("User not found", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        
        if Client.objects.filter(id=id).exists():
            user = Client.objects.get(id=id)
            user.delete()
            return Response("User deleted successfully",status=status.HTTP_200_OK)
        
        return Response("User not found",status=status.HTTP_400_BAD_REQUEST) 



