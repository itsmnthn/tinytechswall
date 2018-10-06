from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()

    country = models.CharField(max_length=30)
    website = models.URLField()

    password = models.CharField(max_length=16)
    recent_passwords = models.CharField(max_length=1000)

    active = models.BooleanField(default=True)
    modified_date = models.DateField()
    registered_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' +self.last_name
