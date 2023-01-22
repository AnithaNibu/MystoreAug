from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    release_date=models.DateField(auto_now_add=True)
    number_of_shows=models.PositiveIntegerField()
    image=models.ImageField(null=True,upload_to="image")
    def __str__(self):
        return self.name
