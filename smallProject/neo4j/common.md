Graph Traversal and Pattern Matching:
Cypher is often used to traverse graphs and match patterns within them. This is useful for querying relationships and nodes based on specific criteria.

Example:
MATCH (p:Person)-[:FRIEND]->(f:Person) <br>
WHERE p.name = 'Alice'  <br>
RETURN f.name   <br>

Creating Nodes and Relationships:
You can use Cypher to create new nodes and relationships in the graph database.

Example:
CREATE (alice:Person {name: 'Alice'})
CREATE (bob:Person {name: 'Bob'})
CREATE (alice)-[:FRIEND]->(bob)
