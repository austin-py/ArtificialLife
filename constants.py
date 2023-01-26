import numpy 


num_steps = 1000 
max_force = 500 
sleep_time = 0.01

amplitude_front = numpy.pi/4 
frequency_front = 50
phaseOffset_front = 0 
targetAngles_front = numpy.linspace(0 , 2*numpy.pi, num = 1000)


amplitude_back = numpy.pi/4 
frequency_back = 50
phaseOffset_back = numpy.pi/8
targetAngles_back = numpy.linspace(0 , 2*numpy.pi, num = 1000)


numberOfGenerations = 1
populationSize = 1


numSensorNeurons = 4 
numMotorNeurons = 3 