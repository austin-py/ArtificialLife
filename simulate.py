from simulation import SIMULATION

def simulate(directOrGUI,solutionID,delete = True):
    simulation = SIMULATION(directOrGUI,int(solutionID),delete=delete)
    simulation.Run()
    simulation.Get_Fitness()