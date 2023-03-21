from django.db import models

# Create your models here.

class Page(models.Model):

    title = models.TextField(max_length=128)
    author = models.TextField(max_length=128, default='johndoe')
    date = models.DateField(max_length=0, null=True)
    text = models.TextField(max_length=1024, default='This is example text')

    def __str__(self):
        return self.title
