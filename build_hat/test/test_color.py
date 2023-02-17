import time
from buildhat import  ColorSensor

cs = ColorSensor('B')
cs.on()
while(1)
    print(cs.get_color())
    time.sleep(1)