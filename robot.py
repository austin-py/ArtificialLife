import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self) -> None:
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_to_Act()
        

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_to_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,t):
        for motor in self.motors:
            self.motors[motor].Set_Value(self.robotId,t)

    def Think(self):
        self.nn.Print()