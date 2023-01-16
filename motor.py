import pybullet as p
import numpy 
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c 

class MOTOR:
    def __init__(self,jointName) -> None:
        self.jointName = jointName
        print(jointName)
        self.motor_values = numpy.linspace(0 , 2*numpy.pi, num = 1000)
        self.Prepare_to_Act()

    def Prepare_to_Act(self):
        self.amplitude = c.amplitude_back
        self.frequency = c.frequency_back
        self.phaseOffset = c.phaseOffset_back

        if self.jointName == 'Torso_BackLeg':
            self.frequency = self.frequency / 2 

        self.motor_values = self.amplitude*numpy.sin(self.frequency*self.motor_values+self.phaseOffset)

    def Set_Value(self,robotId,t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motor_values[t],
            maxForce = c.max_force)
    
    def Save_Values(self):
        numpy.save('data/{self.jointName}Motor.npy',self.motor_values)
