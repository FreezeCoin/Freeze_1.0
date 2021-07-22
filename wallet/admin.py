from django.contrib import admin
from .models import walletDatabase, TokenDetailsDatabase

# Register your models here.
admin.site.register(walletDatabase)
admin.site.register(TokenDetailsDatabase)
