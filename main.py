import search

from simulate import simulate
def main():
    fitness_vals = search.random_evolved()
    print(fitness_vals)

    # simulate('GUI','679',delete=False)
if __name__ == "__main__":
    main()