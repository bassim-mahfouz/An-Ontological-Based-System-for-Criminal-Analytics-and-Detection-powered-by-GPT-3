from Objects import  Entity as EntityFactory 
from Objects import  Relation as RelationFactory 

class TripleMapper:
    def __init__(self):
        self.map = {}
        self.relationSkeletonMapper ={}
        self.create_mapper()
    
    def create_mapper(self):
        # Define the path to your text file
        file_path = "Rules/mapper.txt"

        # Open the file in a try-except block to handle potential errors
        try:
            with open(file_path, "r") as file:
                for line in file:
                    rule=line.strip().split(":")
                    if len(rule) == 2 : 
                        self.map[rule[0]]=rule[1]

        except FileNotFoundError:
            print(f"The file '{file_path}' does not exist.")
        except IOError as e:
            print(f"An error occurred while opening the file: {e}")

    def matchedRule(self,fileName):
        list = fileName.split("-")
        if len(list)>0 :
            return self.map[list[0]]

    def mapEntity(self,rule):
        entity = EntityFactory.Entity()
        ruleList=rule.split("#")
        if len(ruleList) !=2 :
            return None
        entity.label=ruleList[0]
        propertiesMap=ruleList[1].split(",")
        for prop in propertiesMap :
            propList=prop.split(":")
            if len(propList) ==2 :
                column = propList[0]
                propMap=propList[1].split("-")
                if len(propMap) == 2 :
                   entity.propertiesMap[column]={"label" :propMap[0],"type":propMap[1]}
        return entity 

    def relationSkeleton(self,fileName) :
        lineNumber=0
        relationName=""
        startNode=object()
        endNode=object()
        ruleFile =self.matchedRule(fileName)
        
        if self.relationSkeletonMapper.get(ruleFile) is not None:
            return self.relationSkeletonMapper.get(ruleFile)
        else:
            with open(ruleFile, 'r') as file:
                for line in file:
                    if lineNumber==0 :
                        startNode = self.mapEntity(line.strip())
                    if lineNumber==1 :
                        relationName = line.strip()
                    if lineNumber==2 :
                        endNode = self.mapEntity(line.strip())
                    lineNumber+=1

                relation=RelationFactory.Relation()
                relation.name=relationName
                relation.startNode=startNode
                relation.endNode=endNode
                self.relationSkeletonMapper[ruleFile]=relation
                return relation
