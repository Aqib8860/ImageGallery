from django.db import models

# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(null=True)

    def __str__(self):
        return str(self.name)
