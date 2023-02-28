import json 

import helpers.search as search

file_name = 'fitness_vals_temp.json'

def main():
    vals = {}
    for i in range(1):
        fitness_vals = search.random_evolved(show=True)
        vals[i] = fitness_vals
    with open('Data & Diagrams/{}'.format(file_name),'w') as f:
        json.dump(vals,f)

    # simulate('GUI','679',delete=False)
if __name__ == "__main__":
    main()