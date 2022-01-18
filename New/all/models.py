from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class agent(models.Model):
    id = models.AutoField(primary_key=True, unique=True,null=False,)
    telegram_id = models.BigIntegerField( unique=True, null=False, verbose_name='AGENT IDsi')
    name = models.CharField(max_length=400, default='name', null=False, verbose_name='AGENT ISMI')
    tel_num = models.CharField(max_length=50, default='+998912345678',null=False, verbose_name='AGENT TELEFON RAQAMI')
    def __str__(self):
        return f'{self.name}'
class product(models.Model):
    charecter = models.TextField(null=False, blank=False,verbose_name='MAXSULOT XAQIDA')
    id = models.AutoField(primary_key=True, unique=True,null=False)
    image = models.ImageField(upload_to='images',null=False,blank=False,verbose_name='RASM')
    narx = models.IntegerField(verbose_name='NARXI')
    name = models.CharField(max_length=100, default='name', null=False,verbose_name='MAXSULOT NOMI')
    def __str__(self):
        return f'{self.name}'
class orders(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False) #done
    agent = models.ForeignKey(agent,on_delete=models.CASCADE,null=False)
    to_product = models.ForeignKey(product, on_delete=models.CASCADE,null=False)
    money = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now=True,null=False, editable=False) #done
    client_name = models.CharField(max_length=300, default=None)
    client_number = models.CharField(max_length=15, default=None)
    client_addres = models.TextField(default=None)