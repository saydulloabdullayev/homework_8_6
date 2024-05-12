from django.db import models

class Add(models.Model):
    nomi = models.CharField(max_length=100)
    tavsif = models.TextField()

    def __str__(self):
        return self.nomi
    
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='media/themes', default='')
    
    def __str__(self):
        return self.title

class Management(models.Model):
    name= models.CharField(max_length=100)
    number = models.IntegerField()
    
    def __str__(self):
        return self.title
    

class Structura(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)



class Electronic_Fund(models.Model):
    document_number = models.IntegerField()
    keyword = models.CharField(max_length=250)
    doc_category = models.CharField(max_length=250)
    symbol = models.CharField(max_length=250)
    doc_year = models.IntegerField()

    def __str__(self):
        return self.keyword


class Contact(models.Model):
    FIO = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=100)
    managament = models.ForeignKey(Management, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    comments = models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    gmail_2 = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Building(models.Model):
    number = models.IntegerField()
    character = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.characters