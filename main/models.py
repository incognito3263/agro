from django.db import models


class News(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.TextField()
    text = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.name



class Product(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.TextField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name



class Gallery(models.Model):
    photo = models.ImageField(upload_to='images/')


class Send(models.Model):
    full = models.CharField(max_length=205)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.full

class Pdf(models.Model):
    pdf = models.FileField(upload_to='pdf/')
