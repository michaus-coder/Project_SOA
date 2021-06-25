import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    hotel_rpc = RpcProxy('room_service')

    # @http('GET', '/room')
    # def get_rooms(self, request):
    #     rooms = self.hotel_rpc.get_all_room()
    #     return json.dumps(rooms)

    @http('GET', '/room/types')
    def get_room_type(self, request):
        rooms = self.hotel_rpc.get_all_room_type()
        return json.dumps(rooms)

    @http('GET', '/customer/')
    def get_customer(self, request):
        customer = self.hotel_rpc.get_all_customer()
        return json.dumps(customer)

    @http('GET', '/customer/')
    def get_customer_by_id(self, request, customer_id):
        customer = self.hotel_rpc.get_customer_by_id(customer_id)
        return json.dumps(customer)

    # @http('GET', '/room/<string:room_id>')
    # def get_room_by_id(self, request, room_id):
    #     room = self.hotel_rpc.get_room_by_id(room_id)
    #     return json.dumps(room)

    @http('POST', '/room')
    def add_customer(self, request):
        payload = json.loads(request.get_data(as_text=True))
        customer_id = self.hotel_rpc.add_customer(payload['name'], payload['citizen_number'], payload['date_of_birth'], payload['gender'], payload['address'], payload['email'], payload['phone_number1'], payload['phone_number2'], payload['status'], payload['last_update'], payload['last_update_by'])
        return json.dumps(customer_id)

    # @http('DELETE', '/room/<string:room_number>')
    # def delete_room(self, request, room_number):
    #     room_number = self.hotel_rpc.delete_room(room_number)
    #     return "Room with number: " + room_number + " has been successfully deleted."

    # @http('PUT', '/room/<string:room_number>')
    # def change_room_status(self, request, room_number):
    #     room = self.hotel_rpc.change_room_status(room_number)
    #     return json.dumps(room)
