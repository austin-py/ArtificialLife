import os 
from hillclimber import HILL_CLIMBER
from parallelHillclimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# hc = HILL_CLIMBER()
# hc.Evolve()
# hc.Show_Best()


# for i in range(5):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")