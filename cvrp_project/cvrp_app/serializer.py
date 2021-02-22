from django.db.models import fields
from rest_framework import serializers

from .models import tipoDocumento

class tipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoDocumento
        fields = '__all__'