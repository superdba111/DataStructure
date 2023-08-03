from neo4j import GraphDatabase


class AddData:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    @staticmethod
    def _add_data(tx):
        # Sample data
        USERS = [
            {"id": "user1", "name": "John"},
            {"id": "user2", "name": "Sara"},
            {"id": "user3", "name": "Emma"},
            {"id": "user4", "name": "Tom"},
        ]

        AUCTIONS = [
            {"id": "auction1", "date": "2023-08-01"},
            {"id": "auction2", "date": "2023-08-02"},
        ]

        CARS = [
            {
                "id": "car1",
                "make": "Toyota",
                "model": "Corolla",
                "year": 2020,
                "auction_id": "auction1",
            },
            {
                "id": "car2",
                "make": "Honda",
                "model": "Civic",
                "year": 2019,
                "auction_id": "auction2",
            },
        ]

        BIDS = [
            {
                "id": "bid1",
                "amount": 10000,
                "time": "10:00",
                "user_id": "user1",
                "car_id": "car1",
            },
            {
                "id": "bid2",
                "amount": 11000,
                "time": "10:05",
                "user_id": "user2",
                "car_id": "car1",
            },
            {
                "id": "bid3",
                "amount": 10500,
                "time": "10:03",
                "user_id": "user3",
                "car_id": "car1",
            },
            {
                "id": "bid4",
                "amount": 12000,
                "time": "10:07",
                "user_id": "user4",
                "car_id": "car1",
            },
        ]

        ATTENDANCES = [
            {"user_id": "user1", "auction_id": "auction1"},
            {"user_id": "user2", "auction_id": "auction1"},
            {"user_id": "user3", "auction_id": "auction1"},
            {"user_id": "user4", "auction_id": "auction1"},
        ]

        # Create users
        for user in USERS:
            tx.run(
                "CREATE (u:User {id: $id, name: $name})",
                id=user["id"],
                name=user["name"],
            )

        # Create auctions
        for auction in AUCTIONS:
            tx.run(
                "CREATE (a:Auction {id: $id, date: $date})",
                id=auction["id"],
                date=auction["date"],
            )

        # Create cars and assign them to auctions
        for car in CARS:
            tx.run(
                """
                MATCH (a:Auction) WHERE a.id = $auction_id
                CREATE (c:Car {id: $car_id, make: $make, model: $model, year: $year})-[:IS_IN]->(a)
                """,
                auction_id=car["auction_id"],
                car_id=car["id"],
                make=car["make"],
                model=car["model"],
                year=car["year"],
            )

        # Create bids and connect them to users and cars
        for bid in BIDS:
            tx.run(
                """
                MATCH (u:User), (c:Car) WHERE u.id = $user_id AND c.id = $car_id
                CREATE (b:Bid {id: $bid_id, amount: $amount, time: $time})
                CREATE (u)-[:PLACED]->(b)
                CREATE (b)-[:ON]->(c)
                """,
                user_id=bid["user_id"],
                car_id=bid["car_id"],
                bid_id=bid["id"],
                amount=bid["amount"],
                time=bid["time"],
            )

        # Create relationships between users and auctions
        for attendance in ATTENDANCES:
            tx.run(
                """
                MATCH (u:User), (a:Auction) WHERE u.id = $user_id AND a.id = $auction_id
                CREATE (u)-[:ATTENDED]->(a)
                """,
                user_id=attendance["user_id"],
                auction_id=attendance["auction_id"],
            )

    def add_data(self):
        with self._driver.session() as session:
            session.execute_write(self._add_data)


if __name__ == "__main__":
    # MATCH (n) DETACH DELETE n
    data = AddData("bolt://localhost:7687", "neo4j", "password")
    data.add_data()
    data.close()
