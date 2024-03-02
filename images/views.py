from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mycampus.settings import DOMAIN
from .models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings

DOMAIN = settings.DOMAIN


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()

            image_url = DOMAIN + image_serializer.data['image']  # type: ignore

            response = {
                'success': 1,
                'file': {
                    'url': image_url
                }
            }

            return Response(response, status=status.HTTP_201_CREATED)

        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
