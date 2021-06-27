from nameko.rpc import rpc, RpcProxy
from nameko.events import event_handler
import json
import sys


class PO_Orchestration:
    name = 'po_orchestration_service'

    po_service = RpcProxy('po_service')
    supplier_service = RpcProxy('supplier_service')
    employee_service = RpcProxy('employee_service')
    item_service = RpcProxy('item_service')

    # PubSub for circulation
    @event_handler("po_service", "circulation_item_event")
    def handle_circulation_item(self, purchase_id):
        detail_purchase_order = self.po_service.get_detail_po_by_id(purchase_id)
        for detail in detail_purchase_order:
            self.item_service.update_item(detail['id'], detail['qty'], detail['unit'])
        return "Circulation success"

    #Orchestration purchase order
    @rpc
    def create_po(self, employee_id, supplier_id, detail_purchase_order):
        check_employee = self.employee_service.get_employee_id(employee_id)
        check_supplier = self.supplier_service.get_supplier_id(supplier_id)
        if check_employee == True and check_supplier == True:
            result = self.po_service.create_po(
                employee_id, supplier_id, detail_purchase_order)
            return result
        else:
            return "Employee or supplier invalid"

    @rpc
    def get_report(self, purchase_id):
        purchase_order = self.po_service.get_po_by_id(purchase_id)
        detail_purchase_order = self.po_service.get_detail_po_by_id(purchase_id)
        detail_po_result = []
        for detail in detail_purchase_order:
            item = self.item_service.get_item_by_id(detail['id_item'])
            detail_result = {
                "name" : item['name'],
                "barcode" : item['barcode'],
                "quantity" : detail['qty'],
                "unit" : detail['unit'],
                "price_per_unit" : detail['price_per_unit']
            }
            detail_po_result.append(detail_result)
        employee = self.employee_service.get_employee_by_id(purchase_order['id_employee'])
        supplier = self.supplier_service.get_supplier_by_id(purchase_order['id_supplier'])
        result = {
            "date" : purchase_order['date'],
            "employee" : {
                "name" : employee['name'],
                "date_of_birth" : employee['date_of_birth'],
                "citizen_number" : employee['citizen_number'],
                "gender" : employee['gender'],
                "address" : employee['address'],
                "phone_number_1" : employee['phone_number1'],
                "phone_number_2" : employee['phone_number2'],
                "email" : employee['email']
            },
            "supplier" : {
                "name" : supplier['name'],
                "address" : supplier['address'],
                "phone_number_1" : supplier['phone_number1'],
                "phone_number_2" : supplier['phone_number2'],
                "email" : supplier['email']
            },
            "detail_purchase_order" : detail_po_result
        }
        return result
    
    # @rpc
    # def manager_evaluation(self, purchase_order_id, status):
    #     if status == 1:
    #         self.po_service.change_status_po(purchase_order_id, 2)
    #     elif status == 2:
    #         self.po_service.change_status_po(purchase_order_id, 5)

    
