from django.urls import path
from myapp.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('create',UserAPIView.as_view()),
    path('create/<int:id>/',UserAPIView.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/user/',UserAPIView.as_view(),name='user'),
    path('api/change-password/', ChangePassword.as_view(), name='change-password'),
]
