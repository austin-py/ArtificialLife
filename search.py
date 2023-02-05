

from parallelHillclimber import PARALLEL_HILL_CLIMBER

from solution import SOLUTION

def evolve():
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()

def random():
    r = SOLUTION(0)
    r.Evaluate("GUI")


# phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()
# phc.Show_Best()
# hc = HILL_CLIMBER()
# hc.Evolve()
# hc.Show_Best()


# for i in range(5):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")