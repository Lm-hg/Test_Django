from django.db import models
#on crée les caractérisques de ma table 
class Articles(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    date_publication=models.CharField(max_length=100)
