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
    type = "revolute", position = [2.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,0,-.5] , size=[length ,height ,width ])
    pyrosim.End()

create_world()
create_robot()


