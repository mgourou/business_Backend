from django.db import models

# Create your models here.
class Blog(models.Model):
    nom = models.CharField(max_length=30)
    img = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'blog'
        
class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'projet'