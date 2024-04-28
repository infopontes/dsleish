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
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    id_db_original = models.CharField(max_length=5)
    name_chip = models.CharField(max_length=15)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    coat = models.ForeignKey(Coat, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES)
    caracteristics = models.CharField(max_length=300)
    
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse_lazy('animal:animal_detail', kwargs={'pk': self.pk})
    