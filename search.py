from parallelHillclimber import PARALLEL_HILL_CLIMBER
from parallelHillclimber_RandomBodies import PARALLEL_HILL_CLIMBER_RANDOM_BODY

from solution import SOLUTION
from random_solution import RANDOM_SOLUTION

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

def random_evolved():
    phc = PARALLEL_HILL_CLIMBER_RANDOM_BODY()
    phc.Evolve()
    phc.Show_Best()
    return phc.fitness_vals