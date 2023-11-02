import numpy as np

def calculate_parity_bits(data_bits):
    # Рассчитываем количество проверочных битов
    m = 0
    while 2**m <= len(data_bits) + m + 1:
        m += 1
    return m

def hamming_encoding(data_bits):
    # Рассчитываем количество проверочных битов
    m = calculate_parity_bits(data_bits)
    
    # Создаем порождающую матрицу
    G = np.zeros((len(data_bits) + m, len(data_bits)))
    for i in range(len(data_bits)):
        G[i][:] = list(format(i+1, f'0{m}b'))[::-1]
    G[:, m:] = np.eye(m)
    
    # Кодируем информационные биты
    encoded_bits = np.dot(data_bits, G) % 2
    
    # Возвращаем закодированные биты и порождающую матрицу
    return encoded_bits, G

def hamming_decoding(encoded_bits, G):
    # Создаем проверочную матрицу
    H = np.hstack((np.eye(len(encoded_bits[0])), np.transpose(G[:, len(encoded_bits[0]):])))
    
    # Вычисляем синдром
    syndrome = np.dot(encoded_bits, np.transpose(H)) % 2
    
    # Ищем позицию ошибки
    error_position = np.sum(np.multiply(syndrome, 2**np.arange(len(syndrome))[::-1]))
    
    # Исправляем ошибку, если она найдена
    if error_position > 0:
        encoded_bits[error_position-1] = (encoded_bits[error_position-1] + 1) % 2
    
    # Извлекаем информационные биты из закодированных
    decoded_bits = encoded_bits[:, :len(G[0])]
    
    # Возвращаем раскодированные биты
    return decoded_bits

# Шаг 1: Запрос количества информационных разрядов
n = int(input("Введите количество информационных разрядов: "))

# Генерация произвольной информационной комбинации размера n
data_bits = np.random.randint(0, 2, (1, n))

# Шаг 2: Кодирование методом Хемминга
encoded_bits, G = hamming_encoding(data_bits)

print("Закодированные биты:", encoded_bits)

# Шаг 3: Ввод ошибки и исправление
error_position = int(input("Введите позицию ошибки (от 1 до {}): ".format(len(encoded_bits[0]))))
encoded_bits[0][error_position-1] = (encoded_bits[0][error_position-1] + 1) % 2

print("Испорченные биты:", encoded_bits)

# Раскодирование и исправление ошибки
decoded_bits = hamming_decoding(encoded_bits, G)

print("Раскодированные биты:", decoded_bits)