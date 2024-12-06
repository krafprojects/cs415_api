from rest_framework import serializers
from cs415.models import Webuser, Addresstype, Pagedata, Phonetype, Useraddress, Userinfo, Userphone

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webuser
        fields = ["web_user_id", "first_name", "last_name", "email", "created_date", "is_active", "last_login"]

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresstype
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields = '__all__'

class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagedata
        fields = '__all__'
