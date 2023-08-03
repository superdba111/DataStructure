from neo4j import GraphDatabase


class AuctionApp:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def list_auctions(self):
        with self._driver.session() as session:
            result = session.run("MATCH (c:Car) RETURN c")
            return [record["c"]._properties for record in result]

    def place_bid(self, user_id, car_id, amount):
        with self._driver.session() as session:
            session.run(
                "MATCH (user:User {id: $user_id}), (car:Car {id: $car_id}) "
                "CREATE (user)-[:BID {amount: $amount}]->(car)",
                user_id=user_id,
                car_id=car_id,
                amount=amount,
            )

    def highest_bid(self, car_make):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (user:User)-[bid:BID]->(car:Car {make: $car_make}) "
                "RETURN max(bid.amount) AS highest_bid",
                car_make=car_make,
            )
            return result.single()["highest_bid"]

    def highest_bidder(self, car_make):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (user:User)-[bid:BID]->(car:Car {make: $car_make}) "
                "WITH user, bid.amount AS amount "
                "ORDER BY amount DESC "
                "LIMIT 1 "
                "RETURN user.id AS user_id",
                car_make=car_make,
            )
            return result.single()["user_id"]


def main():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "neo4j"  # Change this to your Neo4j password

    app = AuctionApp(uri, user, password)
    print("Available auctions:")
    print(app.list_auctions())

    print("Placing bids...")
    app.place_bid("user1", "car1", 20000)
    app.place_bid("user2", "car2", 21000)

    print("Getting highest bid for Toyota:")
    print(app.highest_bid("Toyota"))

    print("Getting highest bid for Honda:")
    print(app.highest_bid("Honda"))

    print("Getting highest bidder for Toyota:")
    print(app.highest_bidder("Toyota"))

    print("Getting highest bidder for Honda:")
    print(app.highest_bidder("Honda"))


if __name__ == "__main__":
    main()
