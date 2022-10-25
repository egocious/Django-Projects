from email.policy import default
from django.db import models

# Create your models here.
class Artist(models.Model):
   first_name= models.CharField(max_length=50)
   last_name= models.CharField(max_length=50)
   age= models.IntegerField()

   def __str__(self):
    return self.first_name +' '+self.last_name

class Song(models.Model):
    title= models.CharField(max_length=50)
    date_released= models.DateTimeField('date released')
    likes= models.IntegerField(default=0)
    artiste_id= models.ForeignKey(Artist, null='True',on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content= models.TextField()
    song_id= models.ForeignKey(Song, null='True', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    

  

    

   
