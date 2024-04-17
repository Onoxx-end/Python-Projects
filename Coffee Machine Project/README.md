# Coffee Machine Readme

This is a simple Python script that simulates the functionality of a coffee machine. Users can choose from a selection of coffee types (espresso, latte, cappuccino), check the available resources, and receive a report on the machine's current status. The script also allows users to insert coins to pay for their coffee.

## Features

- **Menu:** Users can choose from three types of coffee: espresso, latte, and cappuccino.
- **Resource Management:** The script keeps track of the resources required to make each type of coffee, such as water, milk, and coffee beans. It checks if there are enough resources available before serving the coffee.
- **Payment:** Users can insert coins (pennies, dimes, nickels, and quarters) to pay for their coffee. The script calculates the total amount paid and ensures it matches the cost of the selected coffee.
- **Reporting:** Users can request a report to see the current status of available resources.

## How to Use

1. **Starting the Machine:** Run the script, and the coffee machine will start automatically.
2. **Placing an Order:** Enter the type of coffee you want (espresso, latte, cappuccino) when prompted.
3. **Payment:** Follow the prompts to insert the required coins to pay for your order.
4. **Enjoy Your Coffee:** Once payment is confirmed and resources are available, the coffee will be served.
5. **Checking Resources:** Type "report" to see the current status of available resources.
6. **Ending:** Type "end" to exit the program.

## Requirements

- Python 3.x

## Files

- **menu.py:** Contains the menu of available coffees and their respective ingredients and prices.
- **resources:** Contains the initial amounts of resources available in the coffee machine.
- **coffee_machine.py:** The main script that simulates the coffee machine's functionality.

## Notes

- This script is a simulation and doesn't interact with real hardware.
- You can modify the `resources` dictionary in the `menu.py` file to adjust the initial amounts of resources.
- Feel free to customize the script further to add more features or improve existing functionality.

Enjoy your coffee! ☕️
