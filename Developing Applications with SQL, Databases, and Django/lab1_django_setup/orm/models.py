from django.db import models

class User(models.Model):
    # This is a char field using the type defined by the Django framework to associate with databases.
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)
