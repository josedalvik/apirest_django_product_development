from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from ws.serializers import serializador
from rest_framework.decorators import api_view
import os
import json
import pandas as pd

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        module_dir = os.path.dirname(__file__)  
        cantidad = 100
        xdemo = pd.read_csv(os.path.join(module_dir, '../library/files/X_demo.csv')).reset_index(drop=True)[0:cantidad].to_dict(orient="records")
        ydemo = pd.read_csv(os.path.join(module_dir, '../library/files/y_demo.csv')).reset_index(drop=True)[0:cantidad].to_json(orient="records")
        params = {"xdemo": xdemo, "ydemo": ydemo, "url": request.build_absolute_uri('/')}
        return render(request,"index.html",params)

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
            resultado = ws_serializer.create(ws_serializer.data)
            return JsonResponse(resultado, status=status.HTTP_200_OK)
        return JsonResponse(ws_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
