# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.models import Card
from cards.serializers import CardSerializer
from . import serializers
from django.core import serializers as ss
import json
class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # serializer_class = serializers.CardSerializer
    #
    # def get(self, request, format=None):
    #     cards = Card.objects.all()
    #     data = json.dumps(cards)
    #     data =  ss.serialize(data)
    #     return HttpResponse(data)
    #
    # def post(self, request):
    #     serializer = serializers.CardSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         name = serializer.data.get('name')
    #         email = serializer.data.get('email')
    #         address = serializer.data.get('address')
    #         phoneNumber = serializer.data.get('phoneNumber')
    #         Card.objects.update_or_create(name=name, email=email, address=address, phoneNumber=phoneNumber)
    #         return Response({'message': "hello"})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)