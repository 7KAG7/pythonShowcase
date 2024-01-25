import logging
# set the setpoint temperature to 33
def setpoint_temperature():
    return 33   

# read the current temperature from the sensor
def read_temperature_from_controller():
    return 33    
    



class TempCheck:
    # if the current temp is approaching 20 we need to throw a low temp warning
    @staticmethod
    def low_temp_warning(current_temp):
        return current_temp < 23
    
    # if the current temp is 20 or below we need to throw a low temp alarm
    @staticmethod
    def low_temp_alarm(current_temp):
        return current_temp < 20
    
    # if the current temp is <18 we need to shut down the system
    @staticmethod
    def low_temp_shutdown(current_temp):
        return current_temp < 18
    
    # if the currrent temp is approaching 46 we need to throw a high temp warning
    @staticmethod
    def high_temp_warning(current_temp):
        return current_temp > 43

    # if the current temp is 46 or above we need to throw a high temp alarm
    @staticmethod
    def high_temp_alarm(current_temp):
        return current_temp > 46

    # if the current temp is >48 we need to shut down the system
    @staticmethod
    def high_temp_shutdown(current_temp):
        return current_temp > 48

    @staticmethod
    def main():
        current_temp = read_temperature_from_controller()
        if TempCheck.low_temp_warning(current_temp):
            logging.warning("Low Temp Warning")
        if TempCheck.low_temp_alarm(current_temp):
            logging.warning("Low Temp Alarm")
        if TempCheck.low_temp_shutdown(current_temp):
            logging.warning("Low Temp Shutdown")
        if TempCheck.high_temp_warning(current_temp):
            logging.warning("High Temp Warning")
        if TempCheck.high_temp_alarm(current_temp):
            logging.warning("High Temp Alarm")
        if TempCheck.high_temp_shutdown(current_temp):
            logging.warning("High Temp Shutdown")