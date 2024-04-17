## Bidding Game

This Python script implements a simple bidding game where participants can anonymously submit their bids, and the program determines the highest bidder.

### Instructions

1. **Running the Game:**

   - Run the script in a Python environment.
   - Follow the prompts to enter bidder names and their corresponding bids.
   - When prompted, indicate whether there are any additional bidders.

2. **Winning Bidder:**
   - Once all bids are submitted, the program will display the highest bidder along with their bid.

### Requirements

- Python 3.x

### Usage

1. Clone the repository or download the Python script.
2. Ensure you have Python installed on your system.
3. Execute the script in your preferred Python environment.

### Code Overview

- **`BiddingGame` Class:**

  - `cls()`: Method to clear the console screen.
  - `findHighestBidder(bidder_record)`: Method to find the highest bidder in a dictionary of bidders.

- **Main Logic:**
  - The program welcomes users to the secret auction program.
  - It initializes an empty dictionary to store bidder names and their bids.
  - The bidding process continues until the user indicates no further bidders.
  - Once all bids are collected, the program determines the highest bidder and displays the result.

### Note

- This is a basic implementation and may require additional error handling and features for robustness in a real-world scenario.
- Currently, the program assumes bid amounts are numeric and does not handle non-numeric inputs.

### Example Usage

```
Welcome to the secret auction program.
What is your name?: Alice
What is your bid?: $100
Are there any other bidders? Y/N: Y

What is your name?: Bob
What is your bid?: $150
Are there any other bidders? Y/N: N

The highest bidder was Bob with $150.
Good bye
```

### Disclaimer

- This script is provided as a learning exercise and may not be suitable for production environments without further development and testing.
- Use this script responsibly and ensure compliance with any applicable laws or regulations regarding auctions and bidding.
