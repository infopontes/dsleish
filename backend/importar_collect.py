import csv

import uuid

from backend.collect.models import Collect


def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrderedDict.
    Créditos para Rafael Henrique
    https://bit.ly/2FLDHsH
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        # dt_collection = ''
        # id_search_group = uuid.UUID('3002a552-fbef-45ab-99f5-2f465e702615')
        # id_animal = ''
        animal = str(item.get('ANIMAL'))
        # latitude = ''
        # longitude = ''
        score = 0 if str(item.get('ESCORE'))=='' else int(item.get('ESCORE'))
        serum = True if str(item.get('SORO')) == 'True' else False
        plasma = True if str(item.get('PLASMA')) == 'True' else False
        marrow_aspirate = True if str(item.get('ASPIRADO MEDULA')) == 'True' else False
        lymph_node_aspirate = True if str(item.get('ASPIRADO LINFONODO')) == 'True' else False
        lymph_node_aspirate_dna = str(item.get('DNA ASPIRADO LINFONODO - MF 29'))
        strains = str(item.get('CEPAS'))
        dna_strains = str(item.get('DNA CEPAS'))
        age = str(item.get('IDADE'))
        parasite_slide = str(item.get('PARAS. LAMINA'))
        location_slide = str(item.get('LOCAL'))
        parasite_culture = str(item.get('PARAS. CULTURA'))
        location_culture = str(item.get('LOCAL CULTURA'))
        sorology_rifi = str(item.get('SOROL. RIFI'))
        dilution = 0 if str(item.get('DILUIÇÃO')) == '' else int(item.get('DILUIÇÃO'))
        sorology_dpp = str(item.get('SOROL. DPP'))
        fiocruz_elisa = str(item.get('ELISA FIOCRUZ'))
        biomanguinhos_elisa = str(item.get('ELISA BIOMANGUINHOS'))
        general_state = int(item.get('ESTADO GERAL'))
        ecto_paras = 0 if str(item.get('ECTOPARAS')) == '' else int(item.get('ECTOPARAS'))
        nutritional_status = 0 if str(item.get('EST. NUTRI')) == '' else int(item.get('EST. NUTRI'))
        observation = str(item.get('OBS'))
        coat = 0 if str(item.get('PELAGEM')) == '' else int(item.get('PELAGEM'))
        nails = 0 if str(item.get('UNHAS')) == '' else int(item.get('UNHAS'))
        mucous_coloring = str(item.get('COLOR MUCOSA'))
        muzzle_injury = 0 if str(item.get('LESÃO FOCINHO/ORELHA')) == '' else int(item.get('LESÃO FOCINHO/ORELHA'))
        observation_muzzle_injury = str(item.get('OBS FOCINHO'))
        lymph_node = 0 if str(item.get('LINFONODOS')) == '' else int(item.get('LINFONODOS'))
        observation_lymph_node = str(item.get('OBS LINFONODOS'))
        blepharitis = 0 if str(item.get('BLEFARITE')) == '' else int(item.get('BLEFARITE'))
        conjunctivitis = 0 if str(item.get('CONJUNTIVITE / SERATOCONJUNTIVITE')) == '' else int(item.get('CONJUNTIVITE / SERATOCONJUNTIVITE'))
        observation_conjuntivitis = str(item.get('OBS CONJUNTIVE'))
        alopecia = 0 if str(item.get('ALOPECIA')) == '' else int(item.get('ALOPECIA'))
        observation_alopecia = str(item.get('OBS ALOPECIA'))
        bleeding = 0 if str(item.get('SANGRAMENTO')) == '' else int(item.get('SANGRAMENTO'))
        skin_injury = 0 if str(item.get('LESÃO DE PELE')) == '' else int(item.get('LESÃO DE PELE'))
        observation_skin_injury = str(item.get('OBS PELE'))
        muzzle_depigmentation = 0 if str(item.get('DESPIGMENTAÇÃO FOCINHO/LÁBIO')) == '' else int(item.get('DESPIGMENTAÇÃO FOCINHO/LÁBIO'))
        obj = Collect(
            # dt_collection = dt_collection,
            # id_search_group = id_search_group,
            # id_animal = id_animal,
            animal = animal,
            # latitude = latitude,
            # longitude = longitude,
            score = score,
            serum = serum,
            plasma = plasma,
            marrow_aspirate = marrow_aspirate,
            lymph_node_aspirate = lymph_node_aspirate,
            lymph_node_aspirate_dna = lymph_node_aspirate_dna,
            strains = strains,
            dna_strains = dna_strains,
            age=age,
            parasite_slide = parasite_slide,
            location_slide = location_slide,
            parasite_culture = parasite_culture,
            location_culture = location_culture,
            sorology_rifi = sorology_rifi,
            dilution = dilution,
            sorology_dpp = sorology_dpp,
            fiocruz_elisa = fiocruz_elisa,
            biomanguinhos_elisa = biomanguinhos_elisa,
            general_state = general_state,
            ecto_paras = ecto_paras,
            nutritional_status = nutritional_status,
            observation = observation,
            coat=coat,
            nails = nails,
            mucous_coloring = mucous_coloring,
            muzzle_injury = muzzle_injury,
            observation_muzzle_injury = observation_muzzle_injury,
            lymph_node = lymph_node,
            observation_lymph_node = observation_lymph_node,
            blepharitis = blepharitis,
            conjunctivitis = conjunctivitis,
            observation_conjuntivitis = observation_conjuntivitis,
            alopecia = alopecia,
            observation_alopecia = observation_alopecia,
            bleeding = bleeding,
            skin_injury = skin_injury,
            observation_skin_injury = observation_skin_injury,
            muzzle_depigmentation = muzzle_depigmentation
        )
        aux.append(obj)
    Collect.objects.bulk_create(aux)


data = csv_to_list('dados/collect.csv')
save_data(data)