import os

class BiddingGame:

    def cls():
        '''Clears the console'''
        os.system('cls' if os.name == 'nt' else 'clear')


    def findHighestBidder(bidder_record):
        '''Finds the highest bidder in a dict of bidders'''
        highest_bidder = ""
        highest_bet = 0
        for item in bidder_record:
            if item > highest_bidder:
                highest_bidder = item
                highest_bet = bidder_record[item]
        print(f"The highest bidder was {highest_bidder} with {highest_bet}$.")


    print("Welcome to the secret auction program.")

    bidder_dict = {}
    game_is_active = True

    while game_is_active:
        bidder = input("What is your name?: ")
        bid = input("What is you bid?: $")
        bidder_dict[bidder] = bid
        ongoing = input("Are there any other bidders? Y/N: ")

        if ongoing == "Y":
            cls()
        else:
            findHighestBidder(bidder_dict)
            game_is_active = False
            print("Good bye")

BiddingGame()
