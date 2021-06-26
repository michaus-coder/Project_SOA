import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    po_rpc = RpcProxy('po_service')

    @http('GET', '/purchase_order/')
    def get_po(self, request):
        po = self.po_rpc.get_all_po()
        return json.dumps(po)

    @http('GET', '/purchase_order/<string:id>')
    def get_po(self, id):
        po = self.po_rpc.get_po_by_id(id)
        return json.dumps(po)

    @http('POST', '/purchase_order/')
    def create_po(self, request):
        payload = json.loads(request.get_data(as_text=True))
        new_po = self.po_rpc.create_po(payload['id_employee'], payload['id_supplier'], payload['detail_purchase_order'])
        return new_po

    @http('PUT', '/status_purchase_order/')
    def change_status_po(self, request):
        payload = json.loads(request.get_da(as_text=True))
        change_status = self.po_rpc.change_status_po(payload['id'], payload['status'])
        return json.dumps(change_status)

    @http('PUT', '/purchase_order/')
    def edit_po(self, request):
        payload = json.loads(request.get_da(as_text=True))
        edit = self.po_rpc.edit_po(payload['id'], payload['id_employee'], payload['id_supplier'], payload['status'])
        return json.dumps(edit)

    @http('DELETE', '/purchase_order/<string:id>')
    def delete_po(self, id):
        id = self.po_rpc.delete_po(id)
        return "PO with id: " + id + " has been successfully deleted."
