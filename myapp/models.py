from django.db import models


# Cr eate your models here.
class course(models.Model):
    TopicName=models.CharField(max_length=2000)
    topictitle=models.CharField(max_length=2000)
    tittleDefinition=models.CharField(max_length=2000)
    firstP=models.CharField(max_length=2000)
    firstPExpl=models.CharField(max_length=2000)
    secondp=models.CharField(max_length=2000)
    secondPExp=models.CharField(max_length=2000)

    Explaination=models.CharField(max_length=20000)

    
    
    

    


    

    