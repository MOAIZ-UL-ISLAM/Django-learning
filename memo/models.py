from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs =FileSystemStorage(location = settings.MEDIA_ROOT)




# Create your models here.

class Religion(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Sect(models.Model):
    name = models.CharField(max_length=100)
    religion = models.ForeignKey(Religion,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Caste(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Hobby(models.Model):
    name=models.CharField(max_length=20)
 
    class Meta:
        verbose_name_plural='Hobbies'

    def __str__(self):
        return self.name

class FatherProfile(models.Model):
    name=models.CharField(max_length=200)
    occupation=models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    GENDER_CHOICES= [('M',"male"),('F','female')]
    name=models.CharField(max_length=255,unique=True)
    Profile_pick=models.ImageField(null=True)
    age=models.IntegerField(max_length=30,unique=True)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES ,null=True)
    occupation=models.CharField(max_length=100, null=True)
    is_married=models.BooleanField(default=False)
    birth_date=models.DateField()
    email=models.EmailField(unique=True)
    # Relationships
    religion = models.ForeignKey(Religion,on_delete=models.CASCADE, related_name='profiles',null=True)
    sect = models.ForeignKey(Sect,on_delete=models.CASCADE, related_name='profiles',null=True)
    caste=models.ForeignKey(Caste,on_delete=models.CASCADE,related_name='profiles', null=True)
    hobby=models.ManyToManyField(Hobby, related_name='profiles', null=True)
    father=models.OneToOneField(FatherProfile,on_delete=models.CASCADE, related_name='dependent', null=True)


    def __str__(self):
        return self.name


