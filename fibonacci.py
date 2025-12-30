def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

try:
    user_input = input("Скільки чисел Фібоначчі потрібно? ")
    n_terms = int(user_input)

    if n_terms <= 0:
        print("Введіть число більше нуля.")
    else:
        result = fibonacci(n_terms)
        print(f"Перші {n_terms} чисел Фібоначчі:")
        print(result)

except ValueError:
    print("Помилка, введіть число.")