import numpy 
import random 
import os 
import time

import pyrosim.pyrosim as pyrosim
from simulate import simulate

import constants as c 
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

class RANDOM_SOLUTION():
    def __init__(self, nextAvailableID, seed) -> None:
        self.myID = nextAvailableID
        self.randomSeed = seed
        random.seed(self.randomSeed)
        self.fitness = 0
        self.Create_World()
        self.idNum = 0 
        self.links = []
        self.joints = []
        self.numSensorsNeurons = 0 
        self.numMotorNeurons = 0
        self.Create_Body()
        self.weights = numpy.random.rand(self.numSensorsNeurons,self.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.Create_Brain()
        
       
       

    def Start_Simulation(self,directorgui,bodyID = 0):
        # print('Weights for this round are:', self.weights)
        print("Running simulate")
        # os.system("python3 simulate.py " + directorgui + " " + str(self.myID) + " 2&>1 &")
        simulate(directorgui,str(self.myID),bodyID = str(bodyID))
        print("Command executed") 

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{}.txt".format(self.myID)):
            time.sleep(0.01)
        with open("fitness{}.txt".format(self.myID),'r') as f:
            self.fitness = float(f.read()) 
        os.system("rm fitness{}.txt".format(self.myID))

    def Evaluate(self, directorgui):
        self.Start_Simulation(directorgui)

    def Create_World(self):
       pyrosim.Start_SDF("boxes.sdf")
    #    pyrosim.Send_Cube(name="Box", pos=[-10,10,1.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box1", pos=[-10,10,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box2", pos=[-9,10,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box3", pos=[-9,9,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box4", pos=[-9,11,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box5", pos=[-10,11,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box6", pos=[-10,9,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box7", pos=[-11,11,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box8", pos=[-11,10,.5] , size=[length ,height ,width ])
    #    pyrosim.Send_Cube(name="Box9", pos=[-11,9,.5] , size=[length ,height ,width ])

       pyrosim.End()

# size = depth, width, height 
    def Create_Body(self):
        pyrosim.Start_URDF("body{}.urdf".format(self.myID))
        random_sensor = random.randint(0,10)
        depth = random.random() + 0.01
        width = random.random() * 2 + 0.01 
        height = random.random() + 0.01 
        prev_width = width
        prev_depth = depth 
        prev_height = height 
        prev_direction = 1
        if random_sensor % 2 == 0:
            self.links.append("Torso")
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ], color="green",rgba = ["0","1.0","0","1,0"])
        else:
            pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[depth ,width ,height ])
        random_num_blocks = random.randint(1,10)
        print("Randomly decided on ", random_num_blocks, " blocks")
        parent = "Torso"
        joint_num = 0
        self.numMotorNeurons = random_num_blocks 
        for i in range (random_num_blocks):
            random_sensor = random.randint(0,10)
            if random_sensor % 2 == 0:
                random_sensor = True
            else:
                random_sensor = False
            
            depth = random.random() + 0.01 
            width = random.random() * 2 + 0.01 
            height = random.random() + 0.01 

            direction = random.randint(1,3)

            block_name = "Block" + str(joint_num)
            joint_name = parent + "_" + block_name

            type = 'revolute'
            # floating = random.randint(0,10) % 10 == 0
            # if floating: 
                # type = 'floating'


            if direction == 1:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0.5], jointAxis= '1 0 0')
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
                else:
                    if prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= '1 0 0')
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,prev_height/2], jointAxis= '1 0 0')
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = [0,prev_width/2,0], jointAxis= '1 0 0')   
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,width/2,0],size = [depth,width,height])
            elif direction == 2:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [prev_depth/2,0,0.5], jointAxis= '1 0 0')
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,prev_width/2,0], jointAxis= '1 0 0')
                    elif prev_direction == 3:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth/2,0,prev_height/2], jointAxis= '1 0 0')
                    else:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [prev_depth,0,0], jointAxis= '1 0 0')                       
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [depth/2,0,0],size = [depth,width,height])
            elif direction == 3:
                if i == 0:
                    pyrosim.Send_Joint(name = joint_name   , parent= parent , child = block_name , 
                        type = type, position = [0,0,0.5 + prev_height / 2], jointAxis= '1 0 0')
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])
                else:
                    if prev_direction == 1:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                            type = type, position = [0,prev_width/2,prev_height/2], jointAxis= '1 0 0')
                    elif prev_direction == 2:
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                         type = type, position = (prev_depth/2,0,prev_height/2), jointAxis= '1 0 0')
                    else: 
                        pyrosim.Send_Joint(name = joint_name , parent= parent , child = block_name , 
                        type = type, position = (0,0,prev_height), jointAxis= '1 0 0')
                    if random_sensor:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height],color="green",rgba = ["0","1.0","0","1,0"])
                    else:
                        pyrosim.Send_Cube(name = block_name, pos= [0,0,height/2],size = [depth,width,height])                
            
        

            parent = block_name
            prev_width = width
            prev_depth = depth
            prev_height = height
            prev_direction = direction
            joint_num +=1
            if random_sensor:
                self.links.append(block_name)
                self.numSensorsNeurons +=1
            self.joints.append(joint_name)
        # print(self.joints)
        # print(self.links)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        for link in self.links: 
            pyrosim.Send_Sensor_Neuron(name = self.idNum , linkName = link)
            self.idNum +=1 
            # print("attempted to add link")

        for joint in self.joints:
            pyrosim.Send_Motor_Neuron( name = self.idNum , jointName = joint)
            self.idNum +=1
            # print("attempted to add motor")


        for currentRow in range(self.numSensorsNeurons - 1): 
         for currentColumn in range(self.numMotorNeurons - 1): 
             pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.numSensorsNeurons, weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()

    def Mutate(self):
        try:
            row = random.randint(0,self.numSensorsNeurons - 1)
            column = random.randint(0,self.numMotorNeurons - 1)
            # print("Sensors: ", self.numSensorsNeurons, " Motors: ", self.numMotorNeurons)
            # print("Row: ", row, "Column: ", column )
            # print(self.weights)
            # print(self.weights[row][column])
            self.weights[row][column] =  random.random() * 2 - 1
            # print(self.weights[row][column])
        except ValueError:
            print("FAILED")
            exit()
        

    
    def Set_ID(self, ID):
        self.myID = ID
