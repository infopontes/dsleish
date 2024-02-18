from django.urls import reverse_lazy
from django.db import models
import uuid


from backend.core.models import TimeStampedModel


class Breed(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Breed'
        verbose_name_plural = 'Breeds'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse_lazy('breed:breed_detail', kwargs={'pk': self.pk})