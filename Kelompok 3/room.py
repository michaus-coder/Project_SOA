from nameko.rpc import rpc

import room_dependencies

class RoomService:
    name = 'room_service'

    database = room_dependencies.Database()
    
    #BARUUUUUUUUUUUUUUUUUUUUUU
    #Hanya hard code (statis)
    @rpc
    def get_room_type(self, room_type_name):
        room_type = {
            'id': 1,
            'name' : 'ABCD'
        }
        return room_type

    @rpc
    def get_room_by_type(self, id_room_type):
        room = self.database.get_room(id_room_type)
        return room
    
    #BARUUUUUUUUUUUUUUUUUUUUUU
    #Hanya hard code (statis)
    @rpc
    def get_room_type_by_id (self, id_room_type):
        if id_room_type == 1:
            room_type = {
                'id' : 1,
                'name' : 'Standar Room'
            }
        else:
            room_type = {
                'id' : 2,
                'name' : 'Standard Plus'
            }
        return room_type
