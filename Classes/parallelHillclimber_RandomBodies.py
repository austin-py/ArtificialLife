import copy 
import os 

from Classes.random_solution import RANDOM_SOLUTION
from Classes.constants import Constants

class PARALLEL_HILL_CLIMBER_RANDOM_BODY():
    def __init__(self,seed = None) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")
        self.constants = Constants()
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0
        for i in range(self.constants.populationSize):
            individual_seed = seed + ( i * self.constants.populationSize)
            self.parents[i] = RANDOM_SOLUTION(self.nextAvailableID,seed=individual_seed)
            self.nextAvailableID +=1
        self.child = None
        self.fitness_vals = []

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(self.constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.Save_Best_Fitness_For_Gen()
            self.Print()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Select()
        # self.Select_Best_vs_All()
        # self.Select_Replace_Low_Fitness()
        self.Select_Compare_Pools_of_5()

    def Spawn(self):
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            if self.children[i].weights.all() != self.parents[i].weights.all() and self.children[i].fitness != self.parents[i].fitness:
                print('FAILURE')
                exit()
            self.nextAvailableID +=1

    def showallbest(self):
        self.Evaluate(self.parents,direct = "GUI")

    def Mutate(self):
        for child in self.children.items():
            child[1].Mutate()


    def Select(self):
        for i in range (self.constants.populationSize):
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]      

    def Select_Replace_Low_Fitness(self):
        cutoff = 2
        best_child = self.Find_Best(self.children)
        for i in range(self.constants.populationSize):
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]
            elif self.parents[i].fitness <  cutoff:
                self.parents[i] = best_child   

    def Select_Best_vs_All(self):
        best_parent = self.Find_Best(self.parents)
        best_child = self.Find_Best(self.children)
        if best_child.fitness > best_parent.fitness:
            for i in range (self.constants.populationSize):
                self.parents[i] = best_child

    def Select_Compare_Pools_of_5(self):
        for i in range(int(self.constants.populationSize/5)):
            parents = list(self.parents.items())
            children = list(self.children.items())
            these_parents = dict(parents[i*5:(i*5)+5])
            these_children = dict(children[i*5:(i*5)+5])
            best_parent = self.Find_Best(these_parents)
            best_child = self.Find_Best(these_children)
            if best_child.fitness > best_parent.fitness:
                for i in range (i*5,(i*5) + 5):
                    self.parents[i] = best_child
            

    def Find_Best(self,search_dict):
        min_parent =  None
        min_parent_fitness = 0
        for i in search_dict.items():
            if i[1].fitness > min_parent_fitness:
                min_parent = i[1]
                min_parent_fitness = min_parent.fitness
        return min_parent

    def Show_Best(self):
        min_parent =  self.Find_Best(self.parents)

        print("Our best fitness value was: ", min_parent.fitness)
        min_parent.Create_Brain()
        min_parent.Recreate_Body()
        min_parent.Start_Simulation("GUI")
        min_parent.Wait_For_Simulation_To_End()

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")

        min_parent.Create_Brain()
        min_parent.Recreate_Body()

    def Evaluate(self,solutions,direct = 'DIRECT'):
        for i in solutions.keys():
            solutions[i].Start_Simulation(direct)
        for j in solutions.keys():
            solutions[j].Wait_For_Simulation_To_End()


    def Print(self):
        for i in self.parents.keys():
            print('\n',self.parents[i].fitness,self.children[i].fitness,'\n')

    def Save_Best_Fitness_For_Gen(self):
        min_parent =  self.Find_Best(self.parents)
        self.fitness_vals.append(min_parent.fitness)

