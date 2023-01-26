import numpy 
import pyrosim.pyrosim as pyrosim
import random 
import os 
import time

import constants as c 
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class SOLUTION():
    def __init__(self, nextAvailableID) -> None:
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.fitness = 0
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Start_Simulation(self,directorgui):
        os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &") 

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{}.txt".format(self.myID)):
            time.sleep(0.01)
        with open("fitness{}.txt".format(self.myID),'r') as f:
            self.fitness = float(f.read()) 
            # print(self.fitness)
        os.system("rm fitness{}.txt".format(self.myID))

    def Evaluate(self, directorgui):
        pass
        # os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " &")
        # while not os.path.exists("fitness{}.txt".format(self.myID)):
            # time.sleep(0.01)
        # with open("fitness{}.txt".format(self.myID),'r') as f:
            # self.fitness = float(f.read())

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
       pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])
       pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length ,height ,width ])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
            type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
            type = "revolute", position = [0,-.5,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , 
            type = "revolute", position = [0.5,0,1], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name ="LeftLeg", pos = [0,0.5,1],size=[0.2,1,0.2])
        
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6, jointName= "Torso_LeftLeg" )


        for currentRow in range(c.numSensorNeurons): 
         for currentColumn in range(c.numMotorNeurons): 
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] =  random.random() * 2 - 1

    
    def Set_ID(self, ID):
        self.myID = ID