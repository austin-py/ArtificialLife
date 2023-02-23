from simulation import SIMULATION

def simulate(directOrGUI,solutionID,links,delete = True):
    simulation = SIMULATION(directOrGUI,int(solutionID),links,delete=delete)
    simulation.Run()
    simulation.Get_Fitness()