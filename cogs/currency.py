import random

class Currency:
    def __init__(self):
        self.balance = 0
        self.daily_reward = 100
        self.weekly_reward = 500
        self.monthly_reward = 2000
        self.inventory = []

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposited {amount}. New balance: {self.balance}'
        return 'Deposit amount must be positive.'

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f'Withdrew {amount}. New balance: {self.balance}'
        return 'Withdrawal amount must be positive and less than or equal to balance.'

    def daily(self):
        self.balance += self.daily_reward
        return f'You received your daily reward of {self.daily_reward}. New balance: {self.balance}'

    def weekly(self):
        self.balance += self.weekly_reward
        return f'You received your weekly reward of {self.weekly_reward}. New balance: {self.balance}'

    def monthly(self):
        self.balance += self.monthly_reward
        return f'You received your monthly reward of {self.monthly_reward}. New balance: {self.balance}'

    def work(self):
        earned = random.randint(50, 150)
        self.balance += earned
        return f'You worked and earned {earned}. New balance: {self.balance}'

    def beg(self):
        gained = random.randint(0, 50)
        self.balance += gained
        return f'You begged and received {gained}. New balance: {self.balance}'

    def rob(self, target_balance):
        if target_balance > 0:
            stolen = random.randint(10, target_balance)
            self.balance += stolen
            return f'You robbed a target and gained {stolen}. New balance: {self.balance}'
        return 'Target must have a positive balance to rob.'

    def bankrob(self):
        gain = random.randint(500, 1000)
        self.balance += gain
        return f'You successfully robbed the bank and gained {gain}. New balance: {self.balance}'

    def shop(self, item_cost):
        if item_cost <= self.balance:
            self.balance -= item_cost
            return f'You bought an item for {item_cost}. New balance: {self.balance}'
        return 'Insufficient funds to make the purchase.'

    def add_to_inventory(self, item):
        self.inventory.append(item)
        return f'Added {item} to inventory. Inventory now: {self.inventory}'

    def show_inventory(self):
        return f'Current inventory: {self.inventory}'

# Example of usage:
currency_system = Currency()
# You can now call methods on currency_system to simulate the economy commands
