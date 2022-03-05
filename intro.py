# testing classes


class Test:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_desc(self):
        print(f"First Name: \n{self.first_name.title()} \nLast Name:  \n{self.last_name.title()}")

    def greet(self):
        print(f"\nGood day {self.first_name.title()}!")



user1 = Test('nemuel rico', 'palomo')


user1.show_desc()

user1.greet()