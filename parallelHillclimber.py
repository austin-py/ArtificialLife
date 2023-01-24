import copy 
import os 

from solution import SOLUTION
from constants import numberOfGenerations, populationSize

class PARALLEL_HILL_CLIMBER():
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        self.child = None

    def Evolve(self):
        for i in self.parents.keys():
            # self.parents[i].Evaluate("GUI")
            self.parents[i].Start_Simulation("DIRECT")
        for j in self.parents.keys():
            self.parents[j].Wait_For_Simulation_To_End()
        # for currentGeneration in range(numberOfGenerations):
            # self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        pass
        # self.Spawn()
        # self.Mutate()
        # self.child.Create_Brain()
        # self.child.Evaluate("DIRECT")
        # print('\n',self.parent.fitness, self.child.fitness)
        # self.Select()

    def Spawn(self):
        pass
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID +=1



    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")
