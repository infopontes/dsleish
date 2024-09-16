from django.urls import reverse_lazy
from django.db import models

from backend.breed.models import Breed
from backend.coat.models import Coat

import uuid


from backend.core.models import TimeStampedModel


class Animal(TimeStampedModel):
    
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    id_db_original = models.CharField(max_length=5, blank=True)
    name = models.CharField(max_length=50, blank=True)
    name_chip = models.CharField(max_length=15, blank=True)
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True, blank=True)
    age = models.CharField(max_length=5, blank=True)
    coat = models.ForeignKey(Coat, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    caracteristics = models.CharField(max_length=300, blank=True)
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
    
    def __str__(self):
        return self.name + '- ID DB: ' + self.id_db_original
    
    
    def get_absolute_url(self):
        return reverse_lazy('animal:animal_detail', kwargs={'pk': self.pk})
    