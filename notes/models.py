
from django.db import models
from django.db.models.deletion import CASCADE


class Tag(models.Model):
    Tag = models.CharField(max_length=100)
    def __str__(self):
        tag = self.Tag 
        return(str(tag))



class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=CASCADE)
    def __str__(self):
        id = self.id
        title = self.title
        tag = self.tag
        return(str(id) +" " + str(title)+ " " + str(tag))


