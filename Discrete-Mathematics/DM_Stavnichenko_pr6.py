# Код для построения таблицы простых чисел с помощью решета Эратосфена:

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [i for i in range(n + 1) if primes[i]]
    return prime_numbers

# Построение таблицы простых чисел меньших 256
prime_table = sieve_of_eratosthenes(256)
print("Таблица простых чисел:")
for prime in prime_table:
    print(prime)

# Проверка чисел на простоту с помощью метода Ферма и разложение составных чисел на множители:

import random

def fermat_primality_test(n, k=5):
    if n == 2 or n == 3:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True

def factorize_number(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Проверка чисел на простоту с помощью метода Ферма
numbers = [13, 15, 17, 20]
for number in numbers:
    if fermat_primality_test(number):
        print(number, "является простым числом")
    else:
        print(number, "является составным числом")
        factors = factorize_number(number)
        print("Разложение на множители:", factors)

# Проверка большого простого числа с помощью различных тестов:

import random

def solovay_strassen_primality_test(n, k=5):
    def jacobi_symbol(a, n):
        if a == 0:
            return 0
        if a == 1:
            return 1

        if a % 2 == 0:
            return jacobi_symbol(a // 2, n) * pow(-1, (n * n - 1) // 8)

        if a % n == a:
            return jacobi_symbol(n, a) * pow(-1, ((a - 1) // 2) * ((n - 1) // 2))

        return jacobi_symbol(a % n, n)

    if n == 2:
        return True

    if n % 2 == 0 or n == 1:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, (n - 1) // 2, n)
        if x != 1 and x != n - 1:
            return False

        jacobi = jacobi_symbol(a, n)
        if jacobi == -1:
            jacobi += n

        if x != jacobi:
            return False

    return True

def lehmann_primality_test(n, k=5):
    if n == 2:
        return True

    if n % 2 == 0 or n == 1:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, (n - 1) // 2, n) != 1:
            return False

    return True

def miller_rabin_primality_test(n, k=5):
    def decompose(n):
        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1
        return s, d

    def witness(a, n, s, d):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False

        return True

    if n == 2:
        return True

    if n % 2 == 0 or n == 1:
        return False

    s, d = decompose(n)

    for _ in range(k):
        a = random.randint(2, n - 2)
        if witness(a, n, s, d):
            return False

    return True

def direct_primality_test(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n == 1:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# Проверка большого простого числа с помощью различных тестов
p = 982451653  # Произвольное большое простое число
print("Тест Соловея – Штрассена:", solovay_strassen_primality_test(p))
print("Тест Лемана:", lehmann_primality_test(p))
print("Тест Рабина – Миллера:", miller_rabin_primality_test(p))
print("Непосредственная проверка:", direct_primality_test(p))