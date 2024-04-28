from django.urls import reverse_lazy
from django.db import models
from backend.users.models import User

import uuid

from backend.core.models import TimeStampedModel


class Project(TimeStampedModel):   
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.pk})
    