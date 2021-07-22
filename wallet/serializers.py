from rest_framework import serializers
from .models import walletDatabase, TokenDetailsDatabase


class walletDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = walletDatabase
        fields = '__all__'


class TokenDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenDetailsDatabase
        fields = '__all__'
