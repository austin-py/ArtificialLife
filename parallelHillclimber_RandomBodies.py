import copy 
import os 
import math 
import random 

from random_solution import RANDOM_SOLUTION
from constants import numberOfGenerations, populationSize

class PARALLEL_HILL_CLIMBER_RANDOM_BODY():
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0
        for i in range(populationSize):
            self.parents[i] = RANDOM_SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        self.child = None
        self.fitness_vals = []

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.Save_Best_Fitness_For_Gen()
            self.Print()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()

    def Spawn(self):
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            if self.children[i].weights.all() != self.parents[i].weights.all() and self.children[i].fitness != self.parents[i].fitness:
                print('FAILURE')
                exit()
            self.nextAvailableID +=1



    def Mutate(self):
        for child in self.children.items():
            child[1].Mutate()


    def Select(self):
        for i in range (populationSize):
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]        

    def Show_Best(self):
        min_parent =  None
        min_parent_fitness = 0
        for i in self.parents.items():
            if i[1].fitness > min_parent_fitness:
                min_parent = i[1]
                min_parent_fitness = min_parent.fitness

        print("Our best fitness value was: ", min_parent_fitness)
        min_parent.Create_Brain()
        min_parent.Recreate_Body()
        min_parent.Start_Simulation("GUI")
        min_parent.Wait_For_Simulation_To_End()

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")

        min_parent.Create_Brain()
        min_parent.Recreate_Body()

    def Evaluate(self,solutions):
        for i in solutions.keys():
            solutions[i].Start_Simulation("DIRECT")
        for j in solutions.keys():
            solutions[j].Wait_For_Simulation_To_End()


    def Print(self):
        for i in self.parents.keys():
            print('\n',self.parents[i].fitness,self.children[i].fitness,'\n')

    def Save_Best_Fitness_For_Gen(self):
        min_parent =  None
        min_parent_fitness = 0
        for i in self.parents.items():
            if i[1].fitness > min_parent_fitness:
                min_parent = i[1]
                min_parent_fitness = min_parent.fitness
        self.fitness_vals.append(min_parent_fitness)

