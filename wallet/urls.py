from django.urls import path
from .views import GetUserWalletView, UpdateUserTokensView, UpdateUserFreezeView, GetTokenDetailsView

urlpatterns = [
    path('user', GetUserWalletView.as_view()),
    path('updateUsersTokens', UpdateUserTokensView.as_view()),
    path('updateUsersFreeze', UpdateUserFreezeView.as_view()),
    path('tokenDetails', GetTokenDetailsView.as_view()),
]
