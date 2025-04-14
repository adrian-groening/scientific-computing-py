class Category:

    def __init__(self, name):
        self.ledger = []  
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        """Returns a formatted string representation of the Category."""
        # Title line
        title = f"{self.name:*^30}\n"

        # Ledger lines
        items = ""
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)  # Truncate and left-align
            amount = f"{entry['amount']:.2f}".rjust(7)  # Format and right-align
            items += f"{description}{amount}\n"

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total

# Example Usage
def create_spend_chart(categories):
    """Creates a bar chart showing percentage of spending per category."""
    
    # Step 1: Calculate total spending for each category
    total_spent = []
    for category in categories:
        spent = sum(abs(entry['amount']) for entry in category.ledger if entry['amount'] < 0)
        total_spent.append(spent)

    total = sum(total_spent)  # Sum of all spending
    percentages = [(spent / total) * 100 if total > 0 else 0 for spent in total_spent]  # Percentage spent
    rounded_percentages = [int(p // 10) * 10 for p in percentages]  # Round down to nearest 10%

    # Step 2: Build the chart string
    chart = "Percentage spent by category\n"

    # Add percentage labels and bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "  # Right-align the percentage labels
        for percent in rounded_percentages:
            chart += "o  " if percent >= i else "   "  # Add 'o' if percentage is high enough
        chart += "\n"

    # Step 3: Add the separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 4: Format category names vertically
    max_length = max(len(category.name) for category in categories)  # Find longest category name
    names = [category.name.ljust(max_length) for category in categories]  # Pad shorter names
    
    for i in range(max_length):
        chart += "     "  # Left padding
        for name in names:
            chart += name[i] + "  "  # Add letters with spacing
        chart += "\n"

    return chart.rstrip("\n")  # Remove trailing newline

# Example Usage
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "deposit")
food.withdraw(105.55, "groceries")
food.withdraw(50, "restaurant")

clothing.deposit(500, "deposit")
clothing.withdraw(75.25, "clothes")

auto.deposit(1000, "deposit")
auto.withdraw(175.95, "car repair")

print(create_spend_chart([food, clothing, auto]))

