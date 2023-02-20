import sys 
from simulation import SIMULATION

# directOrGUI = sys.argv[1]
# solutionID = sys.argv[2]
# dont_delete = sys.argv[3]

# simulation = SIMULATION(directOrGUI,int(solutionID))
# simulation.Run()
# simulation.Get_Fitness()

def simulate(directOrGUI,solutionID,bodyID = 0):
    simulation = SIMULATION(directOrGUI,int(solutionID),bodyID=bodyID)
    simulation.Run()
    simulation.Get_Fitness()