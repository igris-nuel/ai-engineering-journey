# class Animal:

#     def __init__(self, name):
#         self.name = name
#         self.list = []

#     def speak(self, sound):
#         print(f"a {self.name} {sound}")
#         self.list.append(sound)


# dog = Animal("dog")
# dog.speak("bark")

# cow = Animal("cow")
# cow.speak("moo")


# print(cow.list)
# print(dog.list)


# print(Animal.speak(Animal("chicken"), "crow"))
# print(chicken.list)


# class BankAccount:
#     def __init__(self, initial_balance: float = 0):
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")

#         self.__balance = initial_balance

#     @property
#     def balance(self) -> float:
#         return self.__balance

#     def _validate_amount(self, amount: float) -> None:
#         if amount <= 0:
#             raise ValueError("Amount must be greater than zero.")

#     def deposit(self, amount: float) -> None:
#         self._validate_amount(amount)
#         self.__balance += amount

#     def withdraw(self, amount: float) -> None:
#         self._validate_amount(amount)

#         if amount > self.__balance:
#             raise ValueError("Insufficient funds.")

#         self.__balance -= amount

# account  = BankAccount(0)

# print(account.balance)

# account.deposit(20000)
# account.withdraw(10000)
# print(account.balance)


class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass


dog = Dog()

dog.eat()