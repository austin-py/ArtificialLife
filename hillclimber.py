from solution import SOLUTION

class HILL_CLIMBER():
    def __init__(self) -> None:
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate()