from django.db import models

# Create your models here.
class Poll (models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
   
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

class Sig (models.Model):
  
    texto= models.TextField(blank=True)

    def __str__(self):
        return f'{self.texto}'

class Mejora (models.Model):
  
    texto= models.TextField(blank=True)

    def __str__(self):
        return f'{self.texto}'

class Covid (models.Model):
  
    texto= models.TextField(blank=True)

    def __str__(self):
        return f'{self.texto}'