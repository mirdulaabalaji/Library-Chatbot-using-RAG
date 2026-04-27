# database/neo4j_loader.py
from neo4j import GraphDatabase

class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def fetch_nodes(self):
        with self.driver.session() as session:
            result = session.run("MATCH (n) RETURN n")
            return [record["n"] for record in result]