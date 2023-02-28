import json 

import helpers.search as search

file_name = 'seed_test1.json'

def main():
    vals = {}
    for seed in range(1):
        fitness_vals = search.random_evolved(show=True,seed = seed)
        vals[seed] = fitness_vals
    with open('Data & Diagrams/{}'.format(file_name),'w') as f:
        json.dump(vals,f)

    # simulate('GUI','679',delete=False)
if __name__ == "__main__":
    main()

    