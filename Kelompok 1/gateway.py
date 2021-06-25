import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http

from werkzeug import Response

import session_dependencies

class ServiceGateway:

    name = 'service_gateway'

    employee_rpc = RpcProxy('service_employee')
    session = session_dependencies.SessionProvider()

    @http('POST', '/api/login')
    def login(self, request):
        username = request.json['username']
        password = request.json['password']
        result = self.employee_rpc.login(username, password)

        response = Response(json.dumps(result), mimetype='application/json')
        if result['status']:
            response.set_cookie('session_id', result['session_id'])
        return response

    @http('POST', '/api/logout')
    def logout(self, request):
        session_id = request.json['session_id']
        result = self.employee_rpc.logout(session_id)

        response = Response(json.dumps(result), mimetype='application/json')
        if result['status']:
            response.set_cookie('session_id', result['session_id'])
        return response
    
    @http('GET', '/api/employee/check')
    def is_logged_in(self, request):
        session_id = request.cookies.get('session_id')
        result = self.employee_rpc.is_logged_in(session_id)
        response = Response(json.dumps({'status': result}), mimetype='application/json')
        return response

    @http('GET', '/api/employee')
    def get_all_employee(self, request):
        session_id = request.cookies.get('session_id')
        result = {
            'status': True,
            'err_msg': '',
            'data': []
        }

        if session_id == '' or session_id is None or (not self.employee_rpc.is_logged_in(session_id)):
            result['status'] = False
            result['err_msg'] = 'You need to login to access this API ' + str(self.session.get_all_online_user())
        else:
            result['data'] = self.employee_rpc.get_all_employee()
        response = Response(json.dumps(result), mimetype='application/json')
        return response

    @http('POST', '/api/forgot_password')
    def forgot_password(self, request):
        id = request.json['id']
        email = request.json['email']

        result = self.employee_rpc.forgot_password(id, email)
        response = Response(json.dumps(result), mimetype='application/json')
        return response

    @http('POST', '/api/employee')
    def get_employee_by_id(self, request, id):
        session_id = request.cookies.get('session_id')
        result = {
            'status': True,
            'err_msg': '',
            'data': []
        }

        if session_id == '' or session_id is None or (not self.employee_rpc.is_logged_in(session_id)):
            result['status'] = False
            result['err_msg'] = 'You need to login to access this API ' + str(self.session.get_all_online_user())
        else:
            result['data'] = self.employee_rpc.get_employee_by_id(id)
        response = Response(json.dumps(result), mimetype='application/json')
        return response

    @http('POST', '/api/register/employee')
    def register_employee(self, request):
        result = self.user_rpc.register_employee(request)
        response = Response(json.dumps({'status' : result}), mimetype='aplication/json')
        return response
    
    @http('POST', '/api/register/employee/account')
    def register_job(self, request):
        result = self.user_rpc.register_job(request)
        response = Response(json.dumps({'status' : result}), mimetype='aplication/json')
        return response

    @http('POST', '/api/register/job')
    def register_job(self, request):
        result = self.user_rpc.register_job(request)
        response = Response(json.dumps({'status' : result}), mimetype='aplication/json') 
        return response

    @http('POST', '/api/employee/edit/data')
    def edit_employee_data(self, request):
        session_id = request.json['session_id']
        id = request.json['id']
        name = request.json['name']
        birth = request.json['birth']
        c_num = request.json['c_num']
        address = request.json['address']
        phone_num1 = request.json['phone_num1']
        phone_num2 = request.json['phone_num2']
        email = request.json['email']

        result = self.employee_rpc.edit_employee_data(session_id, id, name, birth, c_num, address, phone_num1, phone_num2, email)
        response = Response(json.dumps(result), mimetype='application/json')
        return response

    @http('POST', '/api/employee/edit/job')
    def edit_employee_job(self, request):
        session_id = request.json['session_id']
        id = request.json['id']
        id_job = request.json['id_job']
        
        result = self.employee_rpc.edit_employee_job(session_id, id, id_job)
        response = Response(json.dumps(result), mimetype='application/json')
        return response
    
    @http('POST', '/api/employee/edit/status')
    def edit_employee_status(self, request):
        session_id = request.json['session_id']
        id = request.json['id']
        
        result = self.employee_rpc.delete_employee(session_id, id)
        response = Response(json.dumps(result), mimetype='application/json')
        return response