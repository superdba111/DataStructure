from neo4j import GraphDatabase


class AddData:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    @staticmethod
    def create_sample_data(tx):
        # Create Users
        tx.run("CREATE (a:User {id: 'user1', name: 'Alice'})")
        tx.run("CREATE (b:User {id: 'user2', name: 'Bob'})")
        tx.run("CREATE (c:User {id: 'user3', name: 'Charlie'})")

        # Create Cars
        tx.run(
            "CREATE (a:Car {id: 'car1', make: 'Toyota', model: 'Corolla', year: 2020})"
        )
        tx.run("CREATE (b:Car {id: 'car2', make: 'Honda', model: 'Civic', year: 2019})")

        # Create Bids
        tx.run(
            "MATCH (user:User {id: 'user1'}), (car:Car {id: 'car1'}) "
            "CREATE (user)-[:BID {amount: 15000}]->(car)"
        )
        tx.run(
            "MATCH (user:User {id: 'user2'}), (car:Car {id: 'car1'}) "
            "CREATE (user)-[:BID {amount: 16000}]->(car)"
        )
        tx.run(
            "MATCH (user:User {id: 'user3'}), (car:Car {id: 'car2'}) "
            "CREATE (user)-[:BID {amount: 14000}]->(car)"
        )


uri = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"  # Change this to your Neo4j password

add_data = AddData(uri, user, password)
with add_data._driver.session() as session:
    session.execute_write(add_data.create_sample_data)
