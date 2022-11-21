from django.urls import path
from ws.views import vista

urlpatterns = [ 
    path('', vista.index),
    path('prediccion', vista.prediccion),
    path('retroalimentacion', vista.retroalimentacion)
]