class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.kingdomTree = defaultdict(list)
        self.deathTrack = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        
        self.kingdomTree[parentName].append(childName)


    def death(self, name: str) -> None:
        self.deathTrack.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        
        inheritanceOrder = []

        visited = set()
        def getOrder ( name, visited ):
            
            visited.add(name)
            if name not in self.deathTrack:
                inheritanceOrder.append(name)
            
            for childName in self.kingdomTree[name]:
                
                if childName not in visited:
                    getOrder( childName, visited)
        
        getOrder( self.kingName, visited )
        return inheritanceOrder
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()