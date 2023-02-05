from rest_framework.decorators import APIView


class LoginApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        pass
    print("Diwas BAsyal")
    print('My name is Khan.')
