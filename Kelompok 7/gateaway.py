import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    a_rpc = RpcProxy('accident_service')

    @http('POST', '/accident/')
    def create_accident(self, request):
        payload = json.loads(request.get_data(as_text=True))
        accident = self.a_rpc.create_accident(payload['id_booking'], payload['id_employee'], payload['description'], payload['compensation'], payload['compensation_cost'])
        return json.dumps(accident)

    @http('GET', '/accident/')
    def get_compensation(self,request):
        payload = json.loads(request.get_data(as_text=True))
        compensation = self.a_rpc.get_compensation(payload['id_booking'])
        return json.dumps(compensation)

    @http('GET', '/accident/')
    def get_accident_report(self, request):
        payload = json.loads(request.get_data(as_text=True))
        accident_report = self.a_rpc.get_accident_report(payload['start_date'], payload['end_date'])
        return json.dumps(accident_report)

    @http('PUT', '/accident/')
    def update_accident(self, request):
        payload = json.loads(request.get_data(as_text=True))
        update_accident = self.a_rpc.update_accident(payload['id_accident'], payload['status'])
        return json.dumps(update_accident)

    @http('GET', '/accident/')
    def get_all_accident(self, request):
        accident = self.a_rpc.get_all_accident
        return json.dumps(accident)
