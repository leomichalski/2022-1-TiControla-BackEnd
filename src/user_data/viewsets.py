from user_data import serializers
from user_data import models
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from django.contrib.auth import get_user


# classe para mostrar/atualizar os dados do usuario, requer que o usuario esteja autenticado
class UserDataView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserDataSerializer

    def get_object(self):
        # returns the data that belongs to the user
        current_user = get_user(self.request)
        return models.UserData.objects.get(email=current_user.email)

    def post_object(self):
        current_user = get_user(self.request)
        # check if the request email belongs to the user behind it
        if self.request.data['email'] != current_user.email:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        # creates user's data
        models.UserData.objects.post(**self.request.data)
        return Response(None, status=status.HTTP_202_ACCEPTED)

    def put_object(self):
        current_user = get_user(self.request)
        # check if the request email belongs to the user behind it
        if self.request.data['email'] != current_user.email:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        # puts the user's data
        models.UserData.objects.put(**self.request.data)
        return Response(None, status=status.HTTP_202_ACCEPTED)

    def patch_object(self):
        current_user = get_user(self.request)
        # check if the request email belongs to the user behind it
        if self.request.data['email'] != current_user.email:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        # updates the user's data
        models.UserData.objects.get(email=current_user.email).patch(**self.request.data)
        return Response(None, status=status.HTTP_202_ACCEPTED)
