import numpy 

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from Classes.constants import Constants

class MOTOR:
    def __init__(self,jointName) -> None:
        self.constants = Constants()
        self.jointName = jointName
        self.motor_values = numpy.linspace(0 , 2*numpy.pi, num = 1000)
    
    def Set_Value(self,robotId,desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = self.constants.max_force)
