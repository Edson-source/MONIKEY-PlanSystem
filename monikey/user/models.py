from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Personality (models.Model):
    name = models.CharField(max_length=50)
    figure = models.CharField(max_length=50)

class Interest (models.Model):
    name = models.CharField(max_length=50)
    figure = models.CharField(max_length=50)

class Hobbies (models.Model):
    name = models.CharField(max_length=50)
    figure = models.CharField(max_length=50)

class Profile (models.Model):
    CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nao_Binario'),
    )

    image = RichTextUploadingField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=20)
    education = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    birth_date = models.DateField((""), auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=CHOICES, blank=False, null=False)
    twitter = models.URLField((""), max_length=50)
    facebook = models.URLField((""), max_length=50)
    instagram = models.URLField((""), max_length=200)
    bio = models.TextField(max_length=50)

    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    interest = models.ManyToManyField(Interest, on_delete=models.CASCADE)
    hobbies = models.ManyToManyField(Hobbies, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
