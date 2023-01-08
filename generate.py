import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,height,width])

for x_inc in range(5):
    for y_inc in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="Box{}".format(i), pos=[x + x_inc,y + y_inc,z + i] , size=[length - i * 0.1,height - i * 0.1,width - i * 0.1])

pyrosim.End()

