from django.db import models
from django.contrib.auth.models import User


class walletDatabase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UserId = models.AutoField(primary_key=True)
    UserAddress = models.CharField(max_length=500, default='')
    UserTokens = models.CharField(max_length=5000, default='')
    UserSecrete = models.CharField(max_length=3000, default='')
    FroozenNLT = models.FloatField(max_length=100, default='')
    GaruanteedAmt = models.FloatField(max_length=100, default='')
    BorrowaleAmt = models.FloatField(max_length=100, default='')
    ParentAddress = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.UserAddress


class TokenDetailsDatabase(models.Model):
    tokenID = models.AutoField(primary_key=True)
    tokenSymbol = models.CharField(max_length=10)
    tokenName = models.CharField(max_length=50)
    tokenAbi = models.CharField(max_length=5000)
    TokenAddress = models.CharField(max_length=500)
    TokenBlockChain = models.CharField(max_length=10)

    def __str__(self):
        return self.tokenName
