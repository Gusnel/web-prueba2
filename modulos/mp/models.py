from django.db import models
from django.db.models import Max
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image


# Create your models here.

class Mipyme(models.Model):
    class Meta:
            app_label = 'mp'
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    provincia = models.CharField(max_length=30, null=True, blank=True)
    ubicacion = models.CharField(max_length=100, null=True, blank=True)
    num = models.BigIntegerField(default=None, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    valido = models.CharField(max_length=3, default='no')
    imagen = models.ImageField(upload_to='img')
    
 

    def __str__(self):
        txt = "{0} {1} :{2} Ubicacion {3}"
        return txt.format(self.codigo, self.nombre, self.ubicacion, self.num)
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            last_value = Mipyme.objects.aggregate(Max('codigo'))['codigo__max']
            if last_value is None:
                self.codigo = 1
            else:
                self.codigo = last_value + 1
        super().save(*args, **kwargs)

        if self.imagen and isinstance(self.imagen, InMemoryUploadedFile):
            img = Image.open(BytesIO(self.imagen.read()))
            # Realiza cualquier manipulación de la imagen aquí, si es necesario
            img.save(self.imagen.path)

class Producto(models.Model):
    
    id = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.PositiveBigIntegerField(default=0)
    imagen = models.ImageField(upload_to='img')
    mipyme = models.ForeignKey(Mipyme, null=False, blank=False, on_delete=models.CASCADE, related_name='product')

    def nombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.nombre, self.precio, self.mipyme)
    
    def __str__(self):
        txt = "{0} $:{1} de {2}"
        return txt.format(self.nombre, self.precio, self.mipyme.nombre)
