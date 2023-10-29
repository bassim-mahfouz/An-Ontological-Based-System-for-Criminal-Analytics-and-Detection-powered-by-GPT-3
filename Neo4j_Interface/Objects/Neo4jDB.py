from neo4j import GraphDatabase

class Neo4jDB:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def run_cypher_query(self, cypher_query):
        with self._driver.session() as session:
            result = session.run(cypher_query)
            return list(result)