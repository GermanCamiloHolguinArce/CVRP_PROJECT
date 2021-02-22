from django.db import models

class tipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, null =False, blank=False, unique=True)
    siglas = models.CharField(max_length=10, null=False, blank=False)
    expedicion = models.DateField()
    alertiy = models.BooleanField(default=True)
    alert6m = models.BooleanField(default=True)
    alert3m = models.BooleanField(default=True)
    alerti1m = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(tipoDocumento,self).save()

    class Meta:
        verbose_name_plural = 'tipoDocumentos'
