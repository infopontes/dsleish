import csv

from backend.animal.models import Animal


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
        id_db_original = str(item.get('ID_BD_ORIGINAL'))
        name = str(item.get('NOME'))
        name_chip = str(item.get('CHIP_NOME'))
        sex = str(item.get('SEXO'))
        age = str(item.get('IDADE'))
        obj = Animal(
            id_db_original = id_db_original,
            name = name,
            name_chip = name_chip,
            sex = sex,
            age = age
        )
        aux.append(obj)
    Animal.objects.bulk_create(aux)


data = csv_to_list('dados/animal.csv')
save_data(data)