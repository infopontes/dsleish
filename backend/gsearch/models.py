from django.urls import reverse_lazy
from django.db import models

from backend.project.models import Project
from backend.users.models import User

import uuid


from backend.core.models import TimeStampedModel


class Gsearch(TimeStampedModel):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projetos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Gsearch'
        verbose_name_plural = 'Gsearchs'
        unique_together = ('project', 'user')
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse_lazy('gsearch:gsearch_detail', kwargs={'pk': self.pk})
    