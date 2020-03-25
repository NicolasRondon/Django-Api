from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related('user')

    def retrieve(self, request, username, *args, **kwargs):
        try:
            profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('Un perfil con este usuario no existe')

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
