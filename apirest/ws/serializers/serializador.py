from rest_framework import serializers
from django.db.models.fields import DecimalField, DateTimeField
from rest_framework.renderers import JSONRenderer
from ws.library.tf import ClasificacionMultiple
from datetime import datetime
from ws.models.modelo import Prediccion
import json

tf = ClasificacionMultiple()

class prediccion(serializers.Serializer):
    alpha = serializers.DecimalField(30, 23)
    delta = serializers.DecimalField(30, 23)
    u = serializers.DecimalField(30, 23)
    g = serializers.DecimalField(30, 23)
    r = serializers.DecimalField(30, 23)
    i = serializers.DecimalField(30, 23)
    z = serializers.DecimalField(30, 23)
    redshift = serializers.DecimalField(30, 23)
    fecha_creacion = serializers.DateTimeField(required=False, format=None, input_formats=['iso-8601', "%Y-%m-%d %H:%M:%S"])  
    galaxy = serializers.DecimalField(4, 3, required=False)
    qso = serializers.DecimalField(4, 3, required=False)
    star = serializers.DecimalField(4, 3, required=False)
    valor_real = serializers.CharField(required=False)
    fecha_actualizacion = serializers.DateTimeField(required=False, format=None, input_formats=['iso-8601', "%Y-%m-%d %H:%M:%S"])  
    def create(self, validated_data):
        validated_data["fecha_creacion"] = datetime.now()
        #Validando si existe
        prediccion = {}
        try:
            #Existe
            existe = Prediccion.objects.get(alpha=validated_data["alpha"], delta=validated_data["delta"],  u=validated_data["u"], g=validated_data["g"], r=validated_data["r"], i=validated_data["i"], z=validated_data["z"], redshift=validated_data["redshift"])
            prediccion["galaxy"] = existe.galaxy
            prediccion["qso"] = existe.qso
            prediccion["star"] = existe.star
            prediccion["id"] = existe.id
            prediccion["resultado"] = "ok"
        except Prediccion.DoesNotExist:
            #No existe
            jsond = JSONRenderer().render(validated_data)
            prediccion = tf.predict(jsond)
            print("prediccion realizada", prediccion["resultado"])
            if( prediccion["resultado"] == "ok" ):
                print("ok")
                registro = Prediccion.objects.create(**validated_data)
                registro.galaxy = prediccion["galaxy"]
                registro.qso = prediccion["qso"]
                registro.star = prediccion["star"]
                registro.save()
                prediccion["id"] = registro.id
        return prediccion

class retroalimentacion(serializers.Serializer):
    id = serializers.IntegerField()
    valor_real = serializers.CharField(required=True)
    def create(self, validated_data):
        jsond = JSONRenderer().render(validated_data)
        jsond = json.loads(jsond)
        resultado = {"resultado": "ok"}
        try:
            registro = Prediccion.objects.get(id=jsond["id"])
            registro.valor_real = jsond["valor_real"]
            registro.fecha_actualizacion = datetime.now()
            registro.save()
        except Prediccion.DoesNotExist:
            resultado = {"resultado": "not ok"}
        return resultado
            