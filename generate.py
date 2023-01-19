import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

def create_world():
    pyrosim.Start_SDF("boxes.sdf")

    pyrosim.Send_Cube(name="Box", pos=[5,5,5] , size=[length ,height ,width ])

    pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length ,height ,width ])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
        type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length ,height ,width ])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
    type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[length ,height ,width ])
    pyrosim.End()


def Generate_Body():
   pyrosim.Start_URDF("body.urdf")
   pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length ,height ,width ])
   pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
       type = "revolute", position = [1,0,1])
   pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length ,height ,width ])
   pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
   type = "revolute", position = [2,0,1])
   pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[length ,height ,width ])
   pyrosim.End()


def Generate_Brain():
   pyrosim.Start_NeuralNetwork("brain.nndf")

   pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
   pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
   pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

   pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
   pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

   pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -.25 )
   pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 0.25 )

   pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = .25 )
#    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -.25 )
   
   pyrosim.End()


create_world()
Generate_Body()
Generate_Brain()
# create_robot()


