from rolepermissions.roles import AbstractUserRole

class Researcher(AbstractUserRole):
    available_permissions = {
        'read_animal_record': True,
        'read_breed_record': True,
        'read_coat_record': True,
        'read_gsearch_record': True,
        'read_project_record': True,
        'read_specie_record': True,
        
        'create_animal_record': True,
        'create_breed_record': True,
        'create_coat_record': True,
        'create_gsearch_record': True,
        'create_project_record': True,
        'create_specie_record': True,
        
        'update_animal_record': True,
        'update_breed_record': True,
        'update_coat_record': True,
        'update_gsearch_record': True,
        'update_project_record': True,
        'update_specie_record': True,
        
    }

class Student(AbstractUserRole):
    available_permissions = {
        'read_animal_record': True,
        'read_breed_record': True,
        'read_coat_record': True,
        'read_gsearch_record': True,
        'read_project_record': True,
        'read_specie_record': True,
        
        'create_animal_record': False,
        'create_breed_record': False,
        'create_coat_record': False,
        'create_gsearch_record': False,
        'create_project_record': False,
        'create_specie_record': False,
        
        'update_animal_record': False,
        'update_breed_record': False,
        'update_coat_record': False,
        'update_gsearch_record': False,
        'update_project_record': False,
        'update_specie_record': False,
        

    }