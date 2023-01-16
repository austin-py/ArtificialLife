import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random 
import numpy
import time 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("boxes.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitude_front = numpy.pi/4 
frequency_front = 50
phaseOffset_front = 0 
targetAngles_front = numpy.linspace(0 , 2*numpy.pi, num = 1000)
targetAngles_front = amplitude_front*numpy.sin(frequency_front*targetAngles_front+phaseOffset_front)

amplitude_back = numpy.pi/4 
frequency_back = 50
phaseOffset_back = numpy.pi/8
targetAngles_back = numpy.linspace(0 , 2*numpy.pi, num = 1000)
targetAngles_back = amplitude_back*numpy.sin(frequency_back*targetAngles_back+phaseOffset_back)
# numpy.save('data/targetvalues_back.npy',targetAngles_back)
# numpy.save('data/targetvalues_front.npy',targetAngles_front)
# exit()

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_back[i],
        maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_front[i],
        maxForce = 500)

    time.sleep(0.1)

numpy.save('data/backvalues.npy',backLegSensorValues)
numpy.save('data/frontvalues.npy',frontLegSensorValues)
# numpy.save('data/targetvalues.npy',targetAngles)
print(backLegSensorValues)




p.disconnect()