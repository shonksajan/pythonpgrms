class plant:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.machines = []
    def addMachines(self,machine):
        self.machines.append(machine)
class Machine:
    def __init__(self,name,model):
        self.name = name
        self.model = model
        self.spares =[]
        super().__init__(name,model)

    def addSpares(self,spare_parts):
        self.spares.append(spare_parts)
    
class spares:
    def __init__(self,name,weight,price):
        self.name =name
        self.weight = weight
        self.price = price
        super().__init__(name,weight,price)
        
class Spares(Machine):
    def __init__(self,name,partno):
         self.name =name
         self.partno = partno
class Pump(Machine):
    def __init__(self, name, power):
        super().__init__(name, power)