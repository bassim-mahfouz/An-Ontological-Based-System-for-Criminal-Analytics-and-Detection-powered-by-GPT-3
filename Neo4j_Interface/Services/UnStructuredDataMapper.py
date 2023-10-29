import os
from Services import GPTInterface ,SchemaBuilder
from Objects import  Neo4jDB as Neo4jDBFactory
import re

db = Neo4jDBFactory.Neo4jDB("bolt://localhost:7687", "neo4j", "B@ssim1234")


def integrate_text_files_from_directory(directory_path):

    files = os.listdir(directory_path)
    for file in files:
        with open(os.path.join(directory_path, file), 'r') as file:
            file_contents = file.read()
            prompt =f""" 
                    if i have this tweet :
                    {{
                    {file_contents}
                    }}
                    extract nodes and relation with the help of wikpedia for this tweet and provide a cypher query to insert this nodes and relation in a neo4j graph data base,
                    Please I want the answer containing just the Cypher query and add the word queryStart at the begin of the query and queryEnd when it is finished
                    example queryStart 
                    Match	(n) return n 
                    queryEnd
                    """
            response = GPTInterface.chat_with_gpt(prompt)
#             response="""queryStart
# Merge (user:Person {name: "Ali Al Akbar", id:"LB_749853"})
# Merge (donald:Person {name: "Donald Trump"})
# CREATE (user)-[:ENCOURAGES]->(donald)
# RETURN user, donald
# queryEnd"""
            pattern = r'(?<=queryStart\s)[\s\S]*?(?=\squeryEnd)'
            match = re.search(pattern, response, re.DOTALL)
            cypherQuery=match.group(0)
            result =db.run_cypher_query(cypherQuery)
