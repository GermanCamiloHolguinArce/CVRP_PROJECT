from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import tipoDocumento
from .serializer import tipoDocumentoSerializer

def prueba(request):
    return HttpResponse('primer vista creada')


class tipoDocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = tipoDocumento.objects.all().order_by('id')
    serializer_class = tipoDocumentoSerializer

