import search
import random
def main():
    random.seed(0)
    fitness_vals_seed_0 = search.random_evolved()
    # fitness_vals_seed_1 = search.random_evolved(11)
    # fitness_vals_seed_2 = search.random_evolved(3)
    # fitness_vals_seed_3 = search.random_evolved(4)
    print(fitness_vals_seed_0)
    # fitness_vals_seed_4 = search.random_evolved(5)



if __name__ == "__main__":
    main()