### Generar json Comunas y regiones chile para modelo django

Esto es una herramienta para generar los datos para cargar comunas y regiones a una base de datos de django con este modelo:
```

class Region(models.Model):
    """
    Modelo que representa a las regiones.
    """
    id = models.IntegerField(verbose_name="Numero Región", primary_key=True)
    orden = models.IntegerField(verbose_name="orden region", default=0, unique=True)
    nom_reg = models.CharField(max_length=250, verbose_name="Nombre Región", unique=True)
    
    def __str__(self):
        return self.nom_reg
    
class Comuna(models.Model):
    """
    Modelo que representa a las comunas.
    """
    nom_com = models.CharField(max_length=200, unique=True, verbose_name="Nombre Comuna")
    reg_id = models.ForeignKey(Region, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.nom_com  

```
Para su uso es necesario cambiar la variable `data['model']`
con el nombre del proyecto seguido por la tabla de comuno o region segun sea el caso