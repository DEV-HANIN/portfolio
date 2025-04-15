from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.email}"
