import numpy 
import matplotlib.pyplot as p 

backdata = numpy.load('data/backvalues.npy')
frontdata = numpy.load('data/frontvalues.npy')

p.plot(backdata, label = 'BackLeg Data', linewidth = 3)
p.plot(frontdata, label = 'FrontLeg Data', linewidth = 3)
p.legend()
p.show()