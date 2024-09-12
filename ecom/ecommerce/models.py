from django.db import models
from django.contrib.auth.models import User

class catagory(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to='uploads')
    description=models.TextField(max_length=500,blank=False,null='False')
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')

    def __str__(self):
        return self.name

class products(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to='uploads')
    quantity=models.IntegerField(null=False,blank=False)
    old_price=models.FloatField(null=False,blank=False)
    new_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')
    trend=models.BooleanField(default=False,help_text='0-default,0-trend')

    def __str__(self):
        return self.name


class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(products,on_delete=models.CASCADE)
