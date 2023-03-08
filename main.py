import json 

import helpers.search as search
from helpers.simulate import simulate

file_name = 'AllvGroupsof5SelectStatsFull.json'

def main():
    vals = {}
    for seed in range(300):
        fitness_vals = search.random_evolved(show=False,seed = seed)
        vals[seed] = fitness_vals
    with open('Data/{}'.format(file_name),'w') as f:
        json.dump(vals,f)

    # links = ['Torso','Block0','Block1','Block2','Block3','Block4','Block5','Block6','Block7','Block8','Block9','Block10','Block11','Block12']
    # joints = ['Torso_Block0','Block0_Block1','Block1_Block2','Block2_Block3','Block3_Block4','Block4_Block5','Block5_Block6','Block6_Block7','Block7_Block8','Block8_Block9','Block9_Block10','Block10_Block11','Block611_Block12']
    # simulate('GUI','2223',links, joints, delete=False)
if __name__ == "__main__":
    main()


#After that want to drop to 10 creatures and 10 gens and run 30ish sims to try and get some numbers for stats 
    # - NormalSelectStats.json
    # - ReplaceLowSelectStats.json
    # - SelectBestVAllStats.json
    # - AllvGroupsof5SelectStats.json
