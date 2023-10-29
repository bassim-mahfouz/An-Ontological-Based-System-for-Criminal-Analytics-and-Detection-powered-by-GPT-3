import os
import csv
import Services.TripleMapper as TripleMapperFactory
from Objects import  Neo4jDB as Neo4jDBFactory

def integrate_csv_files_from_directory(directory_path):

    if not os.path.isdir(directory_path):
        return "Invalid directory path"
        
    file_list = os.listdir(directory_path)

    csv_files = [f for f in file_list if f.endswith('.csv')]

    if not csv_files:
        return "No CSV files found in the directory"

    tripleMapper =TripleMapperFactory.TripleMapper()
    for csv_file in csv_files:
        relationSkeleton = tripleMapper.relationSkeleton(csv_file)
        file_path = os.path.join(directory_path, csv_file)
        db = Neo4jDBFactory.Neo4jDB("bolt://localhost:7687", "neo4j", "B@ssim1234")

        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                cypher_query=generateCypherQuery(row,relationSkeleton)
                result = db.run_cypher_query(cypher_query)
                for record in result:
                    entity = record["entity"]
                    print(entity)


def generateCypherQuery(row,relationSkeleton):
    cypher_query = f"""
                MERGE (startNode:{mapEntity(relationSkeleton.startNode,row)})
                CREATE (endNode:{mapEntity(relationSkeleton.endNode,row)})
                CREATE (startNode)-[:{relationSkeleton.name}]->(endNode)
            """
    return cypher_query


def mapEntity(entity,row):
    properties=""
    for key, value in entity.propertiesMap.items():
        if properties != "":
            properties+=","

        if value["type"]=="Integer" :
            properties+=value["label"]+" : "+row[int(key)]
        else :
            if value["type"]=="Date":
                properties+=value["label"]+": date('"+row[int(key)]+"')"
            else :
                properties+=value["label"]+" : '"+row[int(key)]+"'"
    return entity.label+" {"+properties+"}"
