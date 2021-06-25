from nameko.rpc import rpc

import dependencies

#Status Accident
# 0 = Accident belum di kompensasi 
# 1 = Accident sudah di kompensasi

class AccidentService:
        name = 'a_service'

        database = dependencies.Database()