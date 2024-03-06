from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import ClubInteraction, UserInteraction
from .serializers import ClubInteractionSerializer, UserInteractionSerializer
from django.contrib.auth import get_user_model
from club.models import Club

User = get_user_model()


class FollowUser(APIView):
    '''
    FollowUser: This view is used to follow a user
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get_user(self, username):  # type: ignore
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return NotFound

    def post(self, request):
        user = request.user
        following_user_id = request.data.get('following_user_id')
        if user == following_user_id:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        following_user = self.get_user(following_user_id)

        serializer = UserInteractionSerializer(data={
            'user': user.pk,
            'follow_user': following_user.pk  # type: ignore
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {

            'message': f'You are now following\
                {following_user.get_username()}'  # type:ignore
        }
        return Response(response, status=status.HTTP_201_CREATED)


class UnfollowUser(APIView):
    '''
    Unfollow User: This view will handle unfollowing a user
    '''

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return NotFound

    def post(self, request):
        user = request.user
        followed_user = self.get_user(request.data.get('followed_user'))

        try:
            interaction = UserInteraction.objects.get(
                user=user, follow_user=followed_user)
        except UserInteraction.DoesNotExist:
            return Response({'error': 'You are now not following this user'}, status=status.HTTP_400_BAD_REQUEST)

        interaction.delete()
        return Response({'message': 'You have unfollowed this user'}, status=status.HTTP_200_OK)


class FollowClub(APIView):
    '''
    FollowClub: This view is used to follow a club
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get_club(self, club_slug):
        try:
            return Club.objects.get(slug=club_slug)
        except Club.DoesNotExist:
            return NotFound

    def post(self, request):
        user = request.user
        club_slug = request.data.get('club_slug')
        club = self.get_club(club_slug)

        serializer = ClubInteractionSerializer(data={
            'user': user.pk,
            'club_id': club.pk  # type: ignore
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'You are now following this club'}, status=status.HTTP_201_CREATED)


class UnfollowClub(APIView):
    '''
    Unfollow Club: This view will handle unfollowing a club
    '''

    def get_club(self, club_id):
        try:
            return Club.objects.get(id=club_id)
        except Club.DoesNotExist:
            return NotFound

    def post(self, request):
        user = request.user
        club = self.get_club(request.data.get('club_id'))

        try:
            interaction = ClubInteraction.objects.get(
                user=user, club_id=club)
        except ClubInteraction.DoesNotExist:
            return Response({'error': 'You are not following this club'}, status=status.HTTP_400_BAD_REQUEST)

        interaction.delete()
        return Response({'message': 'You have unfollowed this club'}, status=status.HTTP_200_OK)
