from rest_framework import generics

from src.plugins import responses
from src.plugins.message_code import MessageCode
from src.users.serializers import UserRegisterSerializer


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return responses.bad_request(message=serializer.errors)
        serializer.save()
        return responses.ok(serializer.data)


