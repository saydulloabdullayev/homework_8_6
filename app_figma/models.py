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

