from django.db import models

class SuggestionsData(models.Model):
    title = models.CharField(max_length=150,default=" ")  
    description = models.TextField(max_length=400,default=" ") 
    vote = models.IntegerField(default=0)  
    def __str__(self):
        return self.title  
