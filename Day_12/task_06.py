class Being:
  species = "Human" 
  def __init__(self,species):
    self.species = species
print(Being.species) #Human
p1 = Being("A")
print(p1.species) #A

