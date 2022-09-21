from django.db import models

# Create your models here.
class MyWatchListtItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.URLField()
    
    