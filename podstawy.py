# 🧩 1. Funkcje w Pythonie
# Opis: Funkcje pozwalają na wielokrotne użycie kodu i organizację logiki.
# Przykład:

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!

# Ćwiczenia:
#     Napisz funkcję is_even(n) zwracającą True, jeśli liczba jest parzysta.
def is_even(n):
    if n % 2 == 0:
        return f"Liczba {n} jest parzysta."
    else:
        return f"Liczba {n} nie jest parzysta."
is_even(4)
is_even(7)
print("test")

#     Stwórz funkcję fibonacci(n) zwracającą n-ty element ciągu Fibonacciego.
#     Zrób funkcję calculate_area(shape, **kwargs) obsługującą różne figury (np. koło, prostokąt).

# 🧱 2. Klasy w Pythonie (OOP)
# Opis: Klasy pozwalają tworzyć obiekty i modelować zachowania.
# Przykład:

class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says Woof!

# Ćwiczenia:

#     Zdefiniuj klasę Car z metodami start(), stop() i atrybutem speed.
#     Stwórz klasę BankAccount z metodami deposit(), withdraw() i balance.
#     Rozszerz klasę Person o dziedziczenie: Student(Person) z dodatkowym polem school.

# 🔁 3. List Comprehensions
# Opis: Skrócona składnia do tworzenia list.
# Przykład:

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ćwiczenia:
#     Utwórz listę liczb parzystych od 0 do 20.
#     Przefiltruj listę imion, zostawiając tylko te zaczynające się na "A".
#     Zbuduj listę długości słów z tekstu: "Python jest super" → [6, 4, 5].

# 🧙 4. Dekoratory
# Opis: Funkcje modyfikujące inne funkcje — używane np. do logowania, walidacji, cache’owania.
# Przykład:

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper  

@logger
def say_hello():
    print("Hello!") 

say_hello()

# Ćwiczenia:
#     Napisz dekorator timer mierzący czas wykonania funkcji.
#     Stwórz dekorator authenticate sprawdzający, czy użytkownik ma dostęp.
#     Zrób dekorator repeat(n) powtarzający funkcję n razy.

