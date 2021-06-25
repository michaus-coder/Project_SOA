from nameko.rpc import rpc

import dependencies

class Supplier:
    #hanya dihardcode karena kelompok supplier belom
    name = 'supplier_service'

    database = dependencies.Database()
    
    #BARUUUUUUUUUUUUUUUUUUUUUU
    #Hanya hard code (statis)
    @rpc
    def get_supplier_id(self, id_supplier):
        supplier = {
            'id': 1,
            'name' : 'ABCD',
            'address' : 'Jl. Gatot Subroto',
            'phone_number2' : '123',
            'phone_number1': '456',
            'email' : 'c14190133@john.petra.ac.id',
            'status' : 1,
            'last_update' : '2021-06-25',
            'last_update_by' : 1
        }
        return supplier

    # @rpc
    # def get_room_by_type(self, id_room_type):
    #     room = self.database.get_room(id_room_type)
    #     return room
    
    # #BARUUUUUUUUUUUUUUUUUUUUUU
    # #Hanya hard code (statis)
    # @rpc
    # def get_room_type_by_id (self, id_room_type):
    #     if id_room_type == 1:
    #         room_type = {
    #             'id' : 1,
    #             'name' : 'Standar Room'
    #         }
    #     else:
    #         room_type = {
    #             'id' : 2,
    #             'name' : 'Standard Plus'
    #         }
    #     return room_type
