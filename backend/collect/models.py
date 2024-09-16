from django.urls import reverse_lazy
from django.db import models

from backend.gsearch.models import Gsearch
from backend.animal.models import Animal

import uuid


from backend.core.models import TimeStampedModel

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class Collect(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    dt_collection = models.DateField(null=True, blank=True)
    id_search_group = models.ForeignKey(Gsearch, on_delete=models.CASCADE, related_name='gsearch', null=True, blank=True)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animal', null=True, blank=True)
    animal = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    serum = models.BooleanField(null=True, blank=True)
    plasma = models.BooleanField(null=True, blank=True)
    marrow_aspirate = models.BooleanField(null=True, blank=True)
    lymph_node_aspirate = models.BooleanField(null=True, blank=True)
    lymph_node_aspirate_dna = models.CharField(max_length=100, null=True, blank=True)
    strains = models.CharField(max_length=20, null=True, blank=True)
    dna_strains = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=10, null=True, blank=True)
    parasite_slide = models.CharField(max_length=10, null=True, blank=True)
    location_slide = models.CharField(max_length=20, null=True, blank=True)
    parasite_culture = models.CharField(max_length=20, null=True, blank=True)
    location_culture = models.CharField(max_length=20, null=True, blank=True)
    sorology_rifi = models.CharField(max_length=10, null=True, blank=True)
    dilution = models.IntegerField(null=True, blank=True)
    sorology_dpp = models.CharField(max_length=10, null=True, blank=True)
    fiocruz_elisa = models.CharField(max_length=10, null=True, blank=True)
    biomanguinhos_elisa = models.CharField(max_length=10, null=True, blank=True)
    general_state = models.IntegerField(null=True, blank=True)
    ecto_paras = models.IntegerField(null=True, blank=True)
    nutritional_status = models.IntegerField(null=True, blank=True)
    observation = models.CharField(max_length=200, null=True, blank=True)
    coat = models.IntegerField(null=True, blank=True)
    nails = models.IntegerField(null=True, blank=True)
    mucous_coloring = models.CharField(max_length=20, null=True, blank=True)
    muzzle_injury = models.IntegerField(null=True, blank=True)
    observation_muzzle_injury = models.CharField(max_length=200, null=True, blank=True)
    lymph_node = models.IntegerField(null=True, blank=True)
    observation_lymph_node = models.CharField(max_length=200, null=True, blank=True)
    blepharitis = models.IntegerField(null=True, blank=True)
    conjunctivitis = models.IntegerField(null=True, blank=True)
    observation_conjuntivitis = models.CharField(max_length=200, null=True, blank=True)
    alopecia = models.IntegerField(null=True, blank=True)
    observation_alopecia = models.CharField(max_length=200, null=True, blank=True)
    bleeding = models.IntegerField(null=True, blank=True)
    skin_injury = models.IntegerField(null=True, blank=True)
    observation_skin_injury = models.CharField(max_length=100, null=True, blank=True)
    muzzle_depigmentation = models.IntegerField(null=True,blank=True)
    
    
    class Meta:
        ordering = ('dt_collection',)
        verbose_name = 'Collect'
        verbose_name_plural = 'Collects'
    
    def __str__(self):
        return str(self.animal)
    
    
    def get_absolute_url(self):
        return reverse_lazy('collect:collect_detail', kwargs={'pk': self.pk})
    