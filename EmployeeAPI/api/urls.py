from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewSets,EmployeeViewSets

router=routers.DefaultRouter()
router.register(r'companies', CompanyViewSets)
router.register(r'employees', EmployeeViewSets)

urlpatterns = [
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]