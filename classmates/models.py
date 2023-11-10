from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

class Classmate(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('animal', 'Animal'),
    )

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200, default='')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='animal')

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

    def clean(self):
        if self.age < 0:
            raise ValidationError("Age cannot be negative.")
