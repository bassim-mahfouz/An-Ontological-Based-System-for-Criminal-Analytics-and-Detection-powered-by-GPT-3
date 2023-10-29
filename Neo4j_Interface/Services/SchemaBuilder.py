from Objects import  Neo4jDB as Neo4jDBFactory


db = Neo4jDBFactory.Neo4jDB("bolt://localhost:7687", "neo4j", "B@ssim1234")
schema=""

def getLabelList() :
    labels=[]
    result =db.run_cypher_query("CALL db.labels()")
    for label in result :
        labels.append(label[0])
    return labels

def getLabelProperty(label) :
    properties=[]
    result =db.run_cypher_query(f"""MATCH (label:{label})
                                    UNWIND keys(label) AS property
                                    RETURN DISTINCT property""")
    for prop in result :
        properties.append(prop[0])
    return properties

def getRelations(startNode,endNode):
    relations=""
    result =db.run_cypher_query(f"""MATCH (startNode:{startNode})-[r]->(endNode:{endNode})
                                    RETURN DISTINCT type(r) AS relationship_type""")
    if len(result)>0: 
        for relation in result :
            if relations!="" :
                relations+=",\n"
            relations += f"{{name:{relation[0]} ,\n startNode:\"{startNode}\" ,\n endNode:\"{endNode}\" }}"
        return relations
    return ""

def buildSchema ():
    global schema
    if schema != "" :
        return schema
    entities=""
    labels =getLabelList()
    for label in labels:
        if entities!="":
            entities+=",\n"
        props= getLabelProperty(label)
        entities +=f"""{{label : \"{label}\",\n properties : {props} }}"""
    
    relations=""
    for startNode in labels:
        for endNode in labels :
            relation = getRelations(startNode,endNode)
            if relation!="" :
                if relations!="" :
                    relations +=",\n"
                relations += relation

    schema = f"{{ nodes: \n [{entities}] ,\n relations :\n [{relations}] }}"
    return schema
