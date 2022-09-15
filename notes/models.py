from turtle import title
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        id = self.id
        title = self.title
        return(str(id) +" " + str(title))