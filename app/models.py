from django.db import models


class Appoinment(models.Model):
    dept = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact_doc(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name

