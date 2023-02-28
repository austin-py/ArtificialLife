from Old.parallelHillclimber import PARALLEL_HILL_CLIMBER
from Classes.parallelHillclimber_RandomBodies import PARALLEL_HILL_CLIMBER_RANDOM_BODY

from Old.solution import SOLUTION
from Classes.random_solution import RANDOM_SOLUTION

def evolve():
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()

def random():
    r = SOLUTION(0)
    r.Evaluate("GUI")


def random_unevolved():
    r = RANDOM_SOLUTION(0)
    r.Evaluate("GUI")

def random_evolved(show=True):
    phc = PARALLEL_HILL_CLIMBER_RANDOM_BODY()
    phc.Evolve()
    if show:
        phc.Show_Best()
    return phc.fitness_vals