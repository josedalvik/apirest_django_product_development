from rest_framework import serializers
from django.db.models.fields import DecimalField, DateTimeField
from rest_framework.renderers import JSONRenderer
from ws.library.tf import ClasificacionMultiple
from datetime import datetime
from ws.models.modelo import Prediccion

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
        jsond = JSONRenderer().render(validated_data)
        prediccion = tf.predict(jsond)
        if( prediccion["resultado"] == "ok" ):
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