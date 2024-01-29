import time
IOController = __import__('iocontroller').IOController

BIBAG_PRESSURE_LIMIT = 100
BIBAG_PRESSURE_CHECK_INTERVAL = 5

class PressureCheck:
    def __init__(self):
        self.bibag_pressure = 0
        self.bibag_pressure_check_time = 0
        self.bibag_pressure_check_interval = BIBAG_PRESSURE_CHECK_INTERVAL
        self.bibag_pressure_limit = BIBAG_PRESSURE_LIMIT

    def check_bibag_pressure(self, bibag_pressure):
        if self.bibag_pressure_check_time == 0:
            self.bibag_pressure_check_time = time.time()
            self.bibag_pressure = bibag_pressure
            return True
        elif time.time() - self.bibag_pressure_check_time > self.bibag_pressure_check_interval:
            self.bibag_pressure_check_time = time.time()
            if self.bibag_pressure - bibag_pressure > self.bibag_pressure_limit:
                return False
            else:
                self.bibag_pressure = bibag_pressure
                return True
        else:
            return True
        
    def pressure_warning(self, bibag_pressure):
        if bibag_pressure > 80:
            return "Warning: Bibag pressure is too high!"
        else:
            return False
        
    def pressure_alarm(self, bibag_pressure):
        if bibag_pressure > 90:
            return "\033[93mAlarm: Bibag pressure is too high, machine will shutdown!\033[0m"
        else:
            return False
        
    
    def pressure_shutdown(self, bibag_pressure):
        if bibag_pressure > 100:
            def close_valves():
                io_controller = IOController()
                io_controller.close_valves()
            return "\033[91mShutdown: Bibag pressure is too high!\033[0m"
        else:
            return False
        
        
        
        