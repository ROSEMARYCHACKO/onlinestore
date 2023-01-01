from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    specs=models.CharField(max_length=100)
    band=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#orm query for creating a resource
#modelname.objects.create(field1=value1,field2=value2............)

#filter()method--to filter the datas or recoreds
#Mobiles.objects.filter(band="15")

#update()
#Mobiles.objects.filter(id=2).update(band="5G")