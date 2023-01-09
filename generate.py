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
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length ,height ,width ])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , 
        type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="Leg", pos=[1,0,1.5] , size=[length ,height ,width ])
    pyrosim.End()

create_world()
create_robot()


