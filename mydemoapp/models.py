from django.db import models

# Create your models here.
class registration(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.first_name

class add_teacherinfo(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profile_pic=models.FileField()
    email=models.EmailField()
    phone=models.IntegerField()
    room_number=models.IntegerField()
    subject1=models.CharField(max_length=100)
    subject2=models.CharField(max_length=100)
    subject3=models.CharField(max_length=100)
    subject4=models.CharField(max_length=100)
    subject5=models.CharField(max_length=100)

class files(models.Model):
    zip_file=models.FileField()
    info_file=models.FileField()


