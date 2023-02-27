import numpy 
import json
import matplotlib.pyplot as p 

# files = ['fitness_vals.json']
files = ['fitness_vals.json','fitness_vals2.json','fitness_vals10.json','fitness_vals10_2.json','fitness_vals10_3.json']
for file in files:
    with open(file,'r') as f:
        data = json.load(f)

    for key in data.keys():
        p.plot(data[key], label = 'Run Number {}, Evolution Number {}'.format('1',key), linewidth = 2)

# p.legend()
p.show()