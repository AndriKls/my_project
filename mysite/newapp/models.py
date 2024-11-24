from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['title']