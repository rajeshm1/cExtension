import pytest
import os
import platform
import time

import Adafruit_BBIO.GPIO as GPIO

class TestSetup:
    def __init__(self,valve):
        self.valve = valve 
        
    def test_setup_output_key(valve_no):
        GPIO.setup("P9_12", GPIO.OUT)
        assert os.path.exists('/sys/class/gpio/gpio60')
        GPIO.setup("P9_13", GPIO.OUT)
        assert os.path.exists('/sys/class/gpio/gpio31')
        GPIO.setup("P9_11", GPIO.OUT)
        assert os.path.exists('/sys/class/gpio/gpio30')
        GPIO.setup("P9_14", GPIO.OUT)
        assert os.path.exists('/sys/class/gpio/gpio50')
        
             	
        GPIO.output("P9_12", GPIO.LOW)
        GPIO.output("P9_14", GPIO.LOW)
        	
        VAL=valve_no.valve
#        VAL = 1
        VAL_num = 2 ** (VAL-1)        	
        for i in range(8): 
            print(i)        
            if VAL & (1 << (7-i)):		
#                GPIO.output("P9_11", GPIO.HIGH)
                print("ON")	
            else:
                print("NA")
#                GPIO.output("P9_11", GPIO.LOW)
    		
    	
        GPIO.output("P9_13", GPIO.HIGH)
        GPIO.output("P9_12", GPIO.HIGH)
        GPIO.output("P9_13", GPIO.LOW)
        GPIO.output("P9_12", GPIO.LOW)
		
		
        GPIO.output("P9_12", GPIO.HIGH)
        time.sleep(1)
        print("Valve Number is:" + str(VAL_num))
       # return VAL       
#obj=TestSetup()
#print(obj.test_setup_output_key())	

