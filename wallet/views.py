from rest_framework.views import APIView
from rest_framework.response import Response
from .models import walletDatabase, TokenDetailsDatabase
from .serializers import walletDatabaseSerializer, TokenDetailsSerializer


class GetUserWalletView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            email = user.email

            wallet_profile = walletDatabase.objects.get(user=user)
            wallet_profile = walletDatabaseSerializer(wallet_profile)

            return Response({'walletProfile': wallet_profile.data, 'email': str(email)})
        except:
            return Response({'error': 'Something went wrong when retrieving wallet_profile'})


class UpdateUserTokensView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            email = user.email

            data = self.request.data
            NewUserTokens = data['UserTokens']

            walletDatabase.objects.filter(
                user=user).update(UserTokens=NewUserTokens)

            wallet_profile = walletDatabase.objects.get(user=user)
            wallet_profile = walletDatabaseSerializer(wallet_profile)

            return Response({'walletProfile': wallet_profile.data, 'email': str(email)})
        except:
            return Response({'error': 'Something went wrong when trying to update UserTokens'})


class UpdateUserFreezeView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            email = user.email

            data = self.request.data
            NewFroozenNLT = data['FroozenNLT']
            NewGaruanteedAmt = data['GaruanteedAmt']
            NewBorrowaleAmt = data['BorrowaleAmt']

            walletDatabase.objects.filter(user=user).update(
                FroozenNLT=NewFroozenNLT,
                GaruanteedAmt=NewGaruanteedAmt,
                BorrowaleAmt=NewBorrowaleAmt
            )

            wallet_profile = walletDatabase.objects.get(user=user)
            wallet_profile = walletDatabaseSerializer(wallet_profile)

            return Response({'walletProfile': wallet_profile.data, 'email': str(email)})
        except:
            return Response({'error': 'Something went wrong when trying to update UserTokens'})


class GetTokenDetailsView(APIView):
    def get(self, request, format=None):

        data = self.request.data
        tokenSym = data['tokenSymbol']

        try:
            if TokenDetailsDatabase.objects.filter(tokenSymbol=tokenSym).exists():

                tokenDetails = TokenDetailsDatabase.objects.get(
                    tokenSymbol=tokenSym)
                tokenDetails = TokenDetailsSerializer(tokenDetails)

                return Response({'tokenDetails': tokenDetails.data})
            else:
                return Response({'error': 'Token do not Exist'})
        except:
            return Response({'error': 'Something went wrong when retrieving tokenDetails'})
