from django.contrib import admin

from .models import Student
# Register your models here.
admin.site.register(Student)


'''
with the help of admmin.py we are registering our model into database and we will create the superuser to access the portal
with the command python manage.py createsuperuser  
'''