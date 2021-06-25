from nameko.rpc import rpc

from dependencies import dependencies 

class AccidentService:

    name = 'accident_service'

    database = dependencies.Database()

    @rpc
    def create_accident(self, id_booking, id_employee, description, compensation, compensation_cost):
        accident = self.database.create_accident(id_booking, id_employee, description, compensation, compensation_cost)
        return accident

    @rpc
    def get_compensation(self,id_booking):
        compensation = self.database.get_compensation()
        return compensation

    @rpc
    def get_accident_report(self, id_booking):
        accident_report = self.database.get_accident_report()
        return accident_report

    @rpc
    def update_accident(self, status):
        updated_accident = self.database.update_accident(
            status, id)
        return updated_accident

    @rpc
    def get_all_accident(self):
        accident=self.database.get_a

    