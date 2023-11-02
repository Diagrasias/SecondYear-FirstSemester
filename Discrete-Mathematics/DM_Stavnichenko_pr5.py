def generate_table(num_bits):
    table = []
    for i in range(2 ** num_bits):
        binary = bin(i)[2:].zfill(num_bits)
        table.append(list(map(int, binary)))
    return table

def hamming_encode(data):
    num_bits = len(data)
    num_parity_bits = 0
    while 2 ** num_parity_bits <= num_bits + num_parity_bits + 1:
        num_parity_bits += 1
    
    encoded_data = [0] * (num_bits + num_parity_bits)
    encoded_index = 0

    for i in range(1, num_bits + num_parity_bits + 1):
        if i & (i - 1) == 0:  # Проверяем, является ли i степенью двойки
            encoded_data.insert(i - 1, 0)  # Вставляем пустой бит на позицию степени двойки
        else:
            encoded_data[i - 1] = data[encoded_index]
            encoded_index += 1

    for i in range(num_parity_bits):
        parity_index = 2 ** i - 1
        parity = 0
        for j in range(parity_index, len(encoded_data), (2 * parity_index + 2)):
            parity ^= encoded_data[j]
        encoded_data[parity_index] = parity

    return encoded_data

def hamming_decode(encoded_data):
    num_parity_bits = 0
    while 2 ** num_parity_bits < len(encoded_data):
        num_parity_bits += 1
    
    error_index = 0
    for i in range(num_parity_bits):
        parity_index = 2 ** i - 1
        parity = 0
        for j in range(parity_index, len(encoded_data), (2 * parity_index + 2)):
            parity ^= encoded_data[j]
        error_index += parity_index * parity

    if error_index != 0:
        encoded_data[error_index - 1] ^= 1

    decoded_data = []
    for i in range(len(encoded_data)):
        if (i + 1) & (i + 1 - (i + 1) // 2) != 0:
            decoded_data.append(encoded_data[i])

    return decoded_data


# Шаг 1: Генерация таблицы
num_bits = int(input("Введите количество информационных разрядов: "))
table = generate_table(num_bits)
print("Таблица размером", len(table), "x", len(table[0]), "сгенерирована:")
for row in table:
    print(row)

# Шаг 2: Кодирование информационной комбинации
data = [1, 0, 1, 1]  # Произвольная информационная комбинация
encoded_data = hamming_encode(data)
print("Закодированная комбинация:", encoded_data)

# Шаг 3: Внесение ошибки и исправление
error_index = 3  # Индекс разряда, в который вносим ошибку
encoded_data[error_index - 1] ^= 1  # Внесение ошибки
print("Испорченная комбинация:", encoded_data)

decoded_data = hamming_decode(encoded_data)
print("Исправленная комбинация:", decoded_data)