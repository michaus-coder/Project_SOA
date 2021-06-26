from nameko.rpc import rpc

from dependencies import dependencies

class Item:
    #hanya dihardcode karena kelompok supplier belom
    name = 'item_service'

    database = dependencies.Database()
    
    #BARUUUUUUUUUUUUUUUUUUUUUU
    #Hanya hard code (statis)
    @rpc
    def get_item_id(self, id_item):
        item = {
            'id': 1,
            'id_type' : 1,
            'name' : 'ABCD',
            'barcode' : 'ABCD',
            'qty_in_hand' : 123,
            'qty_broken': 456,
            'qty_lost' : 789,
            'unit' : 1,
            'status' : 1,
            'last_update' : '2021-06-25',
            'last_update_by' : 1
        }
        return item

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
