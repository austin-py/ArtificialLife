import json
import matplotlib.pyplot as p 

colors = {'NormalSelectFull.json': 'black',
          'NormalSelectWide.json': 'black',
          'NormalSelectStats.json' : 'black',
          'SelectBestVAllFull.json': 'green',
          'SelectBestVAllWide.json': 'green',
          'SelectBestVAllStats.json': 'green',
          'ReplaceLowSelectFull.json': 'red', 
          'ReplaceLowSelectWide.json': 'red',
          'ReplaceLowSelectStats.json': 'red',
          'AllvGroupsof5SelectFull.json': 'blue',  
          'AllvGroupsof5SelectWide.json': 'blue',
          'AllvGroupsof5SelectStats.json': 'blue'}

# files = ['NormalSelectFull.json','ReplaceLowSelectFull.json',]
# files = ['NormalSelectFull.json','SelectBestVAllFull.json',]
# files = ['NormalSelectFull.json','AllvGroupsof5SelectFull.json']

files = ['NormalSelectWide.json', 'ReplaceLowSelectWide.json']
# files = ['NormalSelectWide.json', 'SelectBestVAllWide.json']
# files = ['NormalSelectWide.json', 'AllvGroupsof5SelectWide.json']

# files = ['NormalSelectWide.json', 'NormalSelectFull.json']
# files = ['ReplaceLowSelectWide.json','ReplaceLowSelectFull.json',]
# files = ['SelectBestVAllWide.json','SelectBestVAllFull.json',]
# files = ['AllvGroupsof5SelectWide.json','AllvGroupsof5SelectFull.json']

# files = ['ReplaceLowSelectFull.json','SelectBestVAllFull.json'] # -> Great Contrast 
# files = ['AllvGroupsof5SelectFull.json','SelectBestVAllFull.json'] 

# files = ['AllvGroupsof5SelectFull.json','ReplaceLowSelectFull.json']

# files = ['AllvGroupsof5SelectFull.json','ReplaceLowSelectFull.json','SelectBestVAllFull.json','NormalSelectFull.json']
# files = ['AllvGroupsof5SelectWide.json','ReplaceLowSelectWide.json','SelectBestVAllWide.json','NormalSelectWide.json']

for file in files:
    my_label = '{}'.format(file[:-5])
    name = 'Data & Diagrams/' + file
    with open(name,'r') as f:
        data = json.load(f)
    # if 'Wide' in file:
        # for key in data.keys():
            # for i in range(275):
                # data[key].append(data[key][-1])

    max_key = None 
    max_fit = 0
    for key in data.keys():
        if data[key][-1] > max_fit:
            max_key = key 
            max_fit = data[key][-1]
        p.plot(data[key], label = my_label, linewidth = 2, color = colors[file]) # Seed Number {}, key
        my_label = "_nolegend_"
    # p.plot(data[max_key], label = '{}'.format(file[:-5],), linewidth = 2, color = colors[file]) #
    # p.plot(data["4"], label = '{}, Seed Number {}'.format(file,4), linewidth = 2) #, color = colors[file])

p.xlabel('Number of Generations')
p.ylabel('Fitness')
p.legend()
p.show()


files = ['AllvGroupsof5SelectFull.json','SelectBestVAllFull.json'] # -> Great Contrast 
