from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework import status, serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView


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

        serializer = self.serializer_class(profile, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def delete(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('No se encontro un perfil para este usuario')

        follower.unfollow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('No se encontro un perfil para este usuario')

        if follower.pk is followee.pk:
            raise serializers.ValidationError('No puedes seguirte a ti mismo.')

        follower.follow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)
