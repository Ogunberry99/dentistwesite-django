from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	subject=models.TextField()
	message=models.TextField()
	def __str__(self):
		return self.name


class Appointment(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	phone=models.IntegerField()
	date=models.CharField(max_length=200)
	your_issue=models.TextField()
