from nameko.rpc import rpc, RpcProxy
import json
import sys


class PO_Orchestration:
    name = 'po_orchestration_service'

    po_service = RpcProxy('po_service')
    supplier_service = RpcProxy('supplier_service')
    employee_service = RpcProxy('employee_service')

    #orchestration purchase order
    @rpc
    def create_po(self, employee_id, supplier_id, detail_purchase_order):
        check_employee = self.employee_service.get_employee_id(employee_id)
        check_supplier = self.supplier_service.get_supplier_id(supplier_id)
        if check_employee == True and check_supplier == True:
            result = self.po_service.create_po(employee_id, supplier_id, detail_purchase_order)
            return result
        else:
            return "Employee or supplier invalid"
    
    @rpc
    def manager_evaluation(self, purchase_order_id, supplier_name, supplier_address, supplier_phone_number_1, supplier_phone_number_2, supplier_email, supplier_last_update_by):
        

    @rpc
    def add_supplier(self, name, address, phone_number1, phone_number2, email, status, last_update, last_update_by):
        id_room_type = self.room_service.get_room_type(room_type_name)['id']
        # masih menunggu microservice 'room_service'
        room = self.room_service.get_room_by_type(id_room_type)

        check = False
        for room_info in room:
            print(room_info['id'])
            check_booking_sebelumnya = self.booking_service.get_booking_by_room(
                room_info['id'], start_date, end_date)
            if check_booking_sebelumnya == True:
                insert_data = self.booking_service.add_booking(
                    1, id_room_type, room_info['id'], 1, start_date, end_date, description, 1)
                check = True
                break

        if check == False:
            return {'status': 0, 'message': 'Maaf, kamar tidak tersedia untuk saat ini'}
        elif check == True:
            return insert_data

    @rpc
    def update_booking_room(self, id_booking):
        id_room_type = self.booking_service.get_booking_by_id(id_booking)[
            'id_room_type']
        start_date = self.booking_service.get_booking_by_id(id_booking)[
            'start_date']
        end_date = self.booking_service.get_booking_by_id(id_booking)[
            'end_date']
        room = self.room_service.get_room_by_type(id_room_type)

        check = False
        for room_info in room:
            print(room_info['id'])
            check_booking_sebelumnya = self.booking_service.get_booking_by_room(
                room_info['id'], start_date, end_date)
            if check_booking_sebelumnya == True:
                update_data = self.booking_service.update_booking_room(
                    id_booking, room_info['id'], id_room_type)
                check = True
                break

        if check == False:
            return {'status': 0, 'message': 'Maaf, penukaran kamar tidak tersedia untuk saat ini'}
        elif check == True:
            return update_data

    #BARUUUUUUUUUUUUUUUUUUUUUU
    @rpc
    def check_order_review(self, ktp):
        id_customer = self.booking_service.get_customer_by_citizenNum(ktp)[
            'id']
        id_booking = self.booking_service.get_booking_by_id_customer(
            id_customer)
        customer_name = self.booking_service.get_customer_by_citizenNum(ktp)[
            'name']  # nama customer

        result = []
        for customer_booking in id_booking:
            id_room_type = self.booking_service.get_booking_by_id(customer_booking['id'])[
                'id_room_type']
            result.append({
                'id': customer_booking['id'],
                'Nama Customer': customer_name,
                'Tipe Kamar yang dipesan': self.room_service.get_room_type_by_id(id_room_type)['name'],
                'Booking Date': customer_booking['booking_date'],
                'Start Date': customer_booking['start_date'],
                'End Date': customer_booking['end_date'],
                'Servis yang dipilih': self.booking_service.get_all_service_by_booking_id(customer_booking['id'])
            })
        return result

        #input: n.rpc.entry_service.entry_booking("Standard Room", "2021-06-07", "2021-06-08", "Saya ingin menginap dengan nyaman")
