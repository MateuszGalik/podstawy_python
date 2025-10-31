# 🧩 1. Funkcje w Pythonie
# Opis: Funkcje pozwalają na wielokrotne użycie kodu i organizację logiki.
# Przykład:
def funkcje_w_pythonie():
    def greet(name):
        return f"Hello, {name}!"
    print(greet("Alice"))  # Output: Hello, Alice!

# funkcje_w_pythonie()

# Ćwiczenia:
#     Napisz funkcję is_even(n) zwracającą True, jeśli liczba jest parzysta.
def parzysta_nieparzysta():
    def is_even(n):
        if n % 2 == 0:
            return f"Liczba {n} jest parzysta."
        else:
            return f"Liczba {n} nie jest parzysta."
    print(is_even(4))
    print(is_even(7))
# parzysta_nieparzysta()

#     Stwórz funkcję fibonacci(n) zwracającą n-ty element ciągu Fibonacciego.
def fib_iteracja():
    """
    ✅ Bardzo szybka
    ✅ Minimalne użycie pamięci
    ✅ Nadaje się do dużych n
    """
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    # Przykład: wypisz pierwsze 10 wyrazów
    fib = []
    for i in range(10):
        fib.append(fibonacci(i))
    print(f"Fibonaci iteracja (10): {fib}")
# fib_iteracja()

def fib_rekurencja():
    """
    ✅ Prosta i elegancka
    ❌ Bardzo wolna dla dużych n
    """
    def fib_recursive(n):
        if n <= 1:
            return n
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    print(f"Fibonaci rekurencja (10): {fib_recursive(9)}")
# fib_rekurencja()

def fib_rekurencja_memoizacja():
    """
    ✅ Dużo szybsza niż czysta rekurencja
    ✅ Zapamiętuje wyniki, więc nie powtarza obliczeń
    ❌ Nadal używa stosu rekurencyjnego
    """
    def fib_memo(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        else:
            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]
    print(f"Finanaci rekurencja z memoizacja (10): {fib_memo(9)}")
# fib_rekurencja_memoizacja()

def fib_tablica():
    """
    ✅ Przejrzyste
    ✅ Można łatwo modyfikować do innych problemów
    ❌ Zużywa więcej pamięci niż wersja iteracyjna
    """
    def fib_tab(n):
        if n <= 1:
            return n
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    print(f"Fibonaci tablica (10): {fib_tab(9)}")
# fib_tablica()


def fib_wzor_bineta():
    """
    ✅ Błyskawiczne obliczenia
    ❌ Może dawać niedokładne wyniki dla dużych n (błędy zaokrągleń)
    """
    def fib_binet(n):
        from math import sqrt
        phi = (1 + sqrt(5)) / 2
        psi = (1 - sqrt(5)) / 2
        return round((phi**n - psi**n) / sqrt(5))
    print(f"Fibonaci wzór Bineta (10): {fib_binet(9)}")
# fib_wzor_bineta()

def fib_generator():
    """
    ✅ Bardzo efektywne pamięciowo
    ✅ Nadaje się do generowania dużych ciągów
    ❌ Trzeba iterować, aby uzyskać konkretne wartości
    """
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    gen = fib_gen()
    fib = [next(gen) for _ in range(10)]
    print(f"Fibonaci generator (10): {fib}")
# fib_generator()

# z wykorzystaniem NumPy

def fib_macierz():
    """
    ✅ Bardzo szybka (logarytmiczna złożoność czasowa)
    ✅ Wykorzystuje potęgowanie macierzy
    ❌ Może wymagać dtype=object dla dużych n, by uniknąć przepełnienia
    """
    import numpy as np
    def fib_matrix(n):
        if n == 0:
            return 0
        M = np.array([[1, 1], [1, 0]], dtype=object)
        result = np.linalg.matrix_power(M, n - 1)
        return result[0][0]
    print(f"Fibonaci macierz (10): {fib_matrix(9)}")
# fib_macierz()

def fib_wektorowo():
    import numpy as np

    def fib_vectorized(n):
        fib = np.zeros(n + 1, dtype=int)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib
    fib_sequence = fib_vectorized(9)
    print(f"Fibonaci wektorowo (10): {fib_sequence.tolist()}")
# fib_wektorowo()
#     Zrób funkcję calculate_area(shape, **kwargs) obsługującą różne figury (np. koło, prostokąt).

def obliczanie_pola():
    
    import math
    def calculate_area(shape, **kwargs):
        shaped = shape.lower()
        if shaped == "circle":
            raius = kwargs['radius']
            area = math.pi * raius ** 2
            # return math.pi * raius ** 2
        elif shaped == "rectangle":
            length = kwargs['length']
            width = kwargs['width']
            area = length * width
            # return length * width
        elif shaped == "triangle":
            base = kwargs['base']
            height = kwargs['height']
            area = 0.5 * base * height
            # return 0.5 * base * height
        elif shaped == "square":
            side = kwargs['side']
            area = side ** 2
            # return side ** 2
        elif shaped ==  "ellipse":
            a = kwargs['a']
            b = kwargs['b']
            area = math.pi * a * b
            # return math.pi * a * b
        elif shaped == "trapezoid":
            a = kwargs['a']
            b = kwargs['b']
            height = kwargs['height']
            area = 0.5 * (a + b) * height
            # return 0.5 * (a + b) * height
        else:
            raise ValueError(f"Nieznany kształt: {shape}")
            # return round(area, 2) # wynik zaokraglamy do dwoch miejsc po przecinku
        return f"{area:.2f}"
        
    print(f"Area of circle with radius 5: {calculate_area('circle', radius=5)}") #78.54
    print(f"Area of rectangle 4x6: {calculate_area('rectangle', length=4, width=6)}") #24.00
    print(f"Area of triangle base 4 height 5: {calculate_area('triangle', base=4, height=5)}")
    print(f"Area of square side 4: {calculate_area('square', side=4)}")
    print(f"Area of ellipse a=3 b=4: {calculate_area('ellipse', a=3, b=4)}")
    print(f"Area of trapezoid a=3 b=5 height=4: {calculate_area('trapezoid', a=3, b=5, height=4)}")
    
    try:
        print(f"Area of circle without radius: {calculate_area('azbest')}")
    except ValueError as ve:
        print(f"Błąd: {ve}")
    except KeyError as ke:
        print(f"Błąd: Brakujący parametr {ke}")
    
    try:
        print(f"Area of circle without radius: {calculate_area('circle')}")
    except ValueError as ve:
        print(f"Błąd: {ve}")
    except KeyError as ke:
        print(f"Błąd: Brakujący parametr {ke}")
    
    # print(f"Area of circle without radius: {calculate_area('circle') }")
# obliczanie_pola()

# 🧱 2. Klasy w Pythonie (OOP)
# Opis: Klasy pozwalają tworzyć obiekty i modelować zachowania.
# Przykład:
def kalasy_w_pythonie():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def introduce(self):
            return f"My name is {self.name} and I am {self.age} years old."

    alice = Person("Alice", 30)
    print(alice.introduce())  # Output: My name is Alice and I am 30 years old.
    class Dog:
        def __init__(self, name):
            self.name = name
        def bark(self):
            print(f"{self.name} says Woof!")

    my_dog = Dog("Buddy")
    my_dog.bark()  # Output: Buddy says Woof!
    
# kalasy_w_pythonie()

# Ćwiczenia:
#     Zdefiniuj klasę Car z metodami start(), stop() i atrybutem speed.
#     Stwórz klasę BankAccount z metodami deposit(), withdraw() i balance.
#     Rozszerz klasę Person o dziedziczenie: Student(Person) z dodatkowym polem school.

# 🔁 3. List Comprehensions
# Opis: Skrócona składnia do tworzenia list.
# Przykład:
def listy_w_pythonie():
    squares = [x**2 for x in range(10)]
    print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# listy_w_pythonie()
# Ćwiczenia:
#     Utwórz listę liczb parzystych od 0 do 20.
#     Przefiltruj listę imion, zostawiając tylko te zaczynające się na "A".
#     Zbuduj listę długości słów z tekstu: "Python jest super" → [6, 4, 5].

# 🧙 4. Dekoratory
# Opis: Funkcje modyfikujące inne funkcje — używane np. do logowania, walidacji, cache’owania.
# Przykład:
def dekoratory():
    def logger(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper  

    @logger
    def say_hello():
        print("Hello!") 

    say_hello()
# dekoratory()
# Ćwiczenia:
#     Napisz dekorator timer mierzący czas wykonania funkcji.
#     Stwórz dekorator authenticate sprawdzający, czy użytkownik ma dostęp.
#     Zrób dekorator repeat(n) powtarzający funkcję n razy.

