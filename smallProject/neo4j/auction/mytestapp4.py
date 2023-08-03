from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    id: str
    name: str


@dataclass
class Car:
    id: str
    make: str
    model: str
    year: int


@dataclass
class Bid:
    user: User
    amount: int


@dataclass
class Auction:
    id: str
    car: Car
    bids: List[Bid] = field(default_factory=list)

    def place_bid(self, user, amount):
        bid = Bid(user, amount)
        self.bids.append(bid)

    def highest_bid(self):
        if not self.bids:
            return None
        highest_bid = max(self.bids, key=lambda bid: bid.amount)
        return highest_bid.amount

    def highest_bidder(self):
        if not self.bids:
            return None
        highest_bid = max(self.bids, key=lambda bid: bid.amount)
        return highest_bid.user


if __name__ == "__main__":
    # Create some users
    user1 = User(id="user1", name="Alice")
    user2 = User(id="user2", name="Bob")

    # Create some cars
    car1 = Car(id="car1", make="Toyota", model="Corolla", year=2020)
    car2 = Car(id="car2", make="Honda", model="Civic", year=2019)

    # Create some auctions
    auctions = [Auction(id="auction1", car=car1), Auction(id="auction2", car=car2)]

    # Users place some bids
    auctions[0].place_bid(user1, 20000)
    auctions[0].place_bid(user2, 21000)
    auctions[1].place_bid(user1, 15000)
    auctions[1].place_bid(user2, 16000)

    # Print auctions and winner information
    for auction in auctions:
        print(
            f"Auction ID: {auction.id}, Car: {auction.car.make} {auction.car.model} {auction.car.year}"
        )
        print(f"Highest bid: {auction.highest_bid()}")
        print(f"Winner: {auction.highest_bidder().name}\n")
