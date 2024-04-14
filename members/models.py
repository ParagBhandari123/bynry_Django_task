# members/models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_id = models.CharField(max_length=20)


class ServiceRequest(models.Model):
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contactnum = models.CharField(max_length=20)
    attachment = models.ImageField(upload_to='attachments/')

# from django.db import models

class Request(models.Model):
    id_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending')  # Add a default value

    def __str__(self):
        return f"Request ID: {self.id}"

    
