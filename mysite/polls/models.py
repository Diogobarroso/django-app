from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
            return self.name

    #def clean_email(self):
    #    data = self.cleaned_data['email']
    #    try:
    #        validate_email(data)