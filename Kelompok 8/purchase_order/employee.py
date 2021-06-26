from nameko.rpc import rpc

from dependencies import dependencies

class Employee:
    #hanya dihardcode karena kelompok employee belom
    name = 'employee_service'

    database = dependencies.Database()
    
    #BARUUUUUUUUUUUUUUUUUUUUUU
    #Hanya hard code (statis)
    @rpc
    def get_employee_id(self, id_employee):  
        employee = {
            'id': 1,
            'id_job' : 1,
            'name' : 'ABCD',
            'date_of_birth' : '2021-06-01',
            'citizen_number': '1',
            'gender': 'Male',
            'address': 'Jl. Agung Wibowo',
            'phone_number2': '0895',
            'phone_number1': '0893',
            'email': 'agungwibowo@gmail.com',
            'status' : 1,
            'last_update' : '2021-06-25',
            'last_update_by' : 1          
        }
        return employee

