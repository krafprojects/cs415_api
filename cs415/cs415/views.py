from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from cs415.models import Webuser, Addresstype, Pagedata, Phonetype, Useraddress, Userinfo, Userphone
from cs415.serializers import WebUserSerializer, WebUserSerializerPost, AddressTypeSerializer, PageDataSerializer, PhoneTypeSerializer, UserAddressSerializer, UserInfoSerializer, UserPhoneSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WebUserAPIView(APIView):
    @swagger_auto_schema(responses={200: WebUserSerializer(many=True)})
    def get(self, request):
        users = Webuser.objects.all()
        serializer = WebUserSerializer(users, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New Web User", request_body=WebUserSerializerPost)
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = WebUserSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class SingleWebUserAPIView(APIView):
    def get(self, request, web_user_id):
        user_data = {}
        user = Webuser.objects.get(web_user_id=web_user_id)
        user_serial = WebUserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = UserAddressSerializer(Useraddress.objects.filter(web_user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserInfoSerializer(Userinfo.objects.filter(web_user=user), many=True)
        user_data.update({"info": info.data})
        phone = UserPhoneSerializer(Userphone.objects.filter(web_user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)
    
    @swagger_auto_schema(operation_description="Update WebUser", request_body=WebUserSerializer)
    def patch(self, request, web_user_id):
        webuser_obj = Webuser.objects.get(web_user_id=web_user_id)
        serializer = WebUserSerializer(webuser_obj, data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class AddressTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: AddressTypeSerializer(many=True)})
    def get(self, request):
        addressType = Addresstype.objects.all()
        serializer = AddressTypeSerializer(addressType, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New Address Type", request_body=AddressTypeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AddressTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
class SingleAddressTypeAPIView(APIView):
    def get(self, request, address_type_id):
        address_type = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddressTypeSerializer(address_type)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Address Type", request_body=AddressTypeSerializer)
    def patch(self,request,address_type_id):
        address_type_obj = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddressTypeSerializer(address_type_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class UserAddressAPIView(APIView):
    @swagger_auto_schema(responses={200: UserAddressSerializer(many=True)})
    def get(self, request):
        userAddress = Useraddress.objects.all()
        serializer = UserAddressSerializer(userAddress, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New User Address", request_body=UserAddressSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
class SingleUserAddressAPIView(APIView):
    def get(self, request, user_address_id):
        user_address = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UserAddressSerializer(user_address)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Address", request_body=UserAddressSerializer)
    def patch(self,request,user_address_id):
        user_address_obj = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UserAddressSerializer(user_address_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class PhoneTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: PhoneTypeSerializer(many=True)})
    def get(self, request):
        phoneType = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phoneType, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New Phone Type", request_body=PhoneTypeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
class SinglePhoneTypeAPIView(APIView):
    def get(self, request, phone_type_id):
        phone_type = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhoneTypeSerializer(phone_type)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Phone Type", request_body=PhoneTypeSerializer)
    def patch(self,request,phone_type_id):
        phone_type_obj = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhoneTypeSerializer(phone_type_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class UserPhoneAPIView(APIView):
    @swagger_auto_schema(responses={200: UserPhoneSerializer(many=True)})
    def get(self, request):
        userPhone = Userphone.objects.all()
        serializer = UserPhoneSerializer(userPhone, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New User Phone", request_body=UserPhoneSerializer)
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = UserPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
   
class SingleUserPhoneAPIView(APIView):
    def get(self, request, user_phone_id):
        user_phone = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserPhoneSerializer(user_phone)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Phone", request_body=UserPhoneSerializer)
    def patch(self,request,user_phone_id):
        user_phone_obj = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserPhoneSerializer(user_phone_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class UserInfoAPIView(APIView):
    @swagger_auto_schema(responses={200: UserInfoSerializer(many=True)})
    def get(self, request):
        userInfo = Userinfo.objects.all()
        serializer = UserInfoSerializer(userInfo, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New User Info", request_body=UserInfoSerializer)
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['modified_date'] = str(datetime.now())
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
class SingleUserInfoAPIView(APIView):
    def get(self, request, user_info_id):
        user_info = Userinfo.objects.get(user_info_id=user_info_id)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Phone", request_body=UserInfoSerializer)
    def patch(self,request,user_info_id):
        user_info_obj = Userinfo.objects.get(user_info_id=user_info_id)
        serializer = UserInfoSerializer(user_info_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class PageDataAPIView(APIView):
    @swagger_auto_schema(responses={200: PageDataSerializer(many=True)})
    def get(self, request):
        pageData = Pagedata.objects.all()
        serializer = PageDataSerializer(pageData, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Add New Page Data", request_body=PageDataSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
class SinglePageDataAPIView(APIView):
    def get(self, request, page_data_id):
        page_data = Pagedata.objects.get(page_data_id=page_data_id)
        serializer = PageDataSerializer(page_data)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Phone", request_body=PageDataSerializer)
    def patch(self,request,page_data_id):
        page_data_obj = Pagedata.objects.get(page_data_id=page_data_id)
        serializer = PageDataSerializer(page_data_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


