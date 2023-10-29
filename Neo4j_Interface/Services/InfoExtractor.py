from Services import GPTInterface ,SchemaBuilder
from Objects import  Neo4jDB as Neo4jDBFactory
import re

db = Neo4jDBFactory.Neo4jDB("bolt://localhost:7687", "neo4j", "B@ssim1234")

def extractKnowledge(prompt):
    schema = SchemaBuilder.buildSchema()

    prompt=f"""
    given this neo4j data base schema :\n{schema} \n , give a corespandent cypher query equivalent to this request : {prompt}
    and Please I want the answer containing just the Cypher query and add the word queryStart at the begin of the query and queryEnd when it is finished
    example queryStart 
            Match(n) return n 
            queryEnd
    """

    response = GPTInterface.chat_with_gpt(prompt)

    pattern = r'(?<=queryStart\s)[\s\S]*?(?=\squeryEnd)'

    match = re.search(pattern, response, re.DOTALL)

    cypherQuery=match.group(0)

    result =db.run_cypher_query(cypherQuery)

    prompt=f""" 
    anwser this question : what are the trip for person with id=LB_2323432
    given this neo4j data base schema :\n{schema} \n 
    and this result for the query correspondent for the question \" {cypherQuery} \" \n : 
    {result}
    """
    
    response = GPTInterface.chat_with_gpt(prompt)
    
    return response


