from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    
    def __str__(self) :
        return self.name

'''
as we are creating this model we need to make sure we migrate this to project (0001_initial.py)
with the help of python manage.py makemigration 
we also have to migrate this file into database to store it permantenly with the help of python manage.py migrate
whenever we are updating this file just make sure we are migrating it 
'''