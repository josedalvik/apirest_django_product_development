from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from ws.serializers import serializador
from rest_framework.decorators import api_view

@api_view(['POST'])
def prediccion(request):
    if request.method == 'POST':
        ws_data = JSONParser().parse(request)
        ws_serializer = serializador.prediccion(data=ws_data)
        if ws_serializer.is_valid():
            prediccion = ws_serializer.create(ws_serializer.data)
            return JsonResponse(prediccion, status=status.HTTP_200_OK)
        return JsonResponse(ws_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def retroalimentacion(request):
    if request.method == 'POST':
        ws_data = JSONParser().parse(request)
        ws_serializer = serializador.retroalimentacion(data=ws_data)
        if ws_serializer.is_valid():
            ws_serializer.create(ws_serializer.data)
            return JsonResponse(ws_serializer.errors, status=status.HTTP_200_OK)
        return JsonResponse(ws_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
