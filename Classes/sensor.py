import numpy 
import pyrosim.pyrosim as pyrosim

from Classes.constants import Constants

class SENSOR:
    def __init__(self,linkName) -> None:
        self.linkName = linkName
        self.constants = Constants()
        self.values = numpy.zeros(self.constants.num_steps)
    
    def Get_Value(self,t):
            self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save('data/{self.linkName}Sensor.npy',self.values)