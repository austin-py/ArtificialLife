import json
import matplotlib.pyplot as p 

colors = {'NormalSelectFull.json': 'blue','SelectBestVAllFull.json': 'green','ReplaceLowSelectFull.json': 'red'}

# files = ['fitness_vals.json']
# files = ['fitness_vals.json','fitness_vals2.json','fitness_vals10.json','fitness_vals10_2.json','fitness_vals10_3.json']

# files = ['ReplaceLowSelect.json','NormalSelect.json','AllvsOneSelect.json',]
files = ['SelectBestVAllFull.json','NormalSelectFull.json']
# files = ['NormalSelectFull.json']
for file in files:
    name = 'Data & Diagrams/' + file
    with open(name,'r') as f:
        data = json.load(f)

    for key in data.keys():
        p.plot(data[key], label = '{}, Seed Number {}'.format(file[:-5],key), linewidth = 2, color = colors[file])
    # p.plot(data["4"], label = '{}, Seed Number {}'.format(file,4), linewidth = 2) #, color = colors[file])

# p.xlabel('Number of Generations')
p.ylabel('Fitness')
# p.legend()
p.show()

#Normal, Replace, All [0,1]
# All, Replace, Normal [2,3] 
#Normal, All, Replace [4]