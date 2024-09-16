from django import forms

from .models import Collect

class CollectForm(forms.ModelForm):

    class Meta:
        model = Collect
        fields = ('dt_collection',
                  'id_search_group',
                  'id_animal',
                  'animal',
                  'latitude',
                  'longitude',
                  'score',
                  'serum',
                  'plasma',
                  'marrow_aspirate',
                  'lymph_node_aspirate',
                  'lymph_node_aspirate_dna',
                  'strains',
                  'dna_strains',
                  'age',
                  'parasite_slide',
                  'location_slide',
                  'parasite_culture',
                  'location_culture',
                  'sorology_rifi',
                  'dilution',
                  'sorology_dpp',
                  'fiocruz_elisa',
                  'biomanguinhos_elisa',
                  'general_state',
                  'ecto_paras',
                  'nutritional_status',
                  'observation',
                  'coat',
                  'nails',
                  'mucous_coloring',
                  'muzzle_injury',
                  'observation_muzzle_injury',
                #   'ear_injury',
                #   'observation_ear_injury',
                  'lymph_node',
                  'observation_lymph_node',
                  'blepharitis',
                  'conjunctivitis',
                  'observation_conjuntivitis',
                  'alopecia',
                  'observation_alopecia',
                  'bleeding',
                  'skin_injury',
                  'observation_skin_injury',
                  'muzzle_depigmentation',
                  )
        
        widgets = {
            "id_search_group": forms.Select(),
            "id_animal": forms.Select(),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['phone_number'].widget.attrs.update({'class': 'mask-phone'})
        