from Classes.simulation import SIMULATION

def simulate(directOrGUI,solutionID,links,joints,delete = True):
    simulation = SIMULATION(directOrGUI,int(solutionID),links,joints,delete=delete)
    if simulation == None: return 
    simulation.Run()
    simulation.Get_Fitness()