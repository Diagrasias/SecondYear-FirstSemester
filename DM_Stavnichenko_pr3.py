import heapq
import math
from collections import Counter

def calculate_entropy(frequencies, text_length):
    entropy = 0
    for freq in frequencies:
        probability = freq / text_length
        entropy -= probability * math.log2(probability)
    return entropy

def huffman_encoding(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def calculate_average_code_length(encoding, frequencies, text_length):
    average_length = 0
    for symbol, code in encoding:
        probability = frequencies[symbol] / text_length
        average_length += probability * len(code)
    return average_length

def calculate_redundancy(alphabet_size, average_code_length):
    return 1 - (math.log2(alphabet_size) / average_code_length)

def encode_text(text, encoding):
    encoded_text = ""
    for char in text:
        for symbol, code in encoding:
            if char == symbol:
                encoded_text += code
                break
    return encoded_text

def decode_text(encoded_text, encoding):
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        for symbol, encoding in encoding:
            if code == encoding:
                decoded_text += symbol
                code = ""
                break
    return decoded_text

def print_encoding(encoding):
    print("Алфавитное кодирование:")
    for symbol, code in encoding:
        print(f"{symbol}: {code}")

# Считываем текст из файла
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read().replace("\n", "")

# Считаем частоту каждого символа в тексте
frequencies = Counter(text)
text_length = len(text)

# Вычисляем энтропию
entropy = calculate_entropy(frequencies.values(), text_length)

# Строим алфавитное кодирование методом Хаффмана
encoding = huffman_encoding(dict(frequencies))
average_code_length = calculate_average_code_length(encoding, frequencies, text_length)

# Вычисляем избыточность
redundancy = calculate_redundancy(len(frequencies), average_code_length)

# Выводим результаты
print(f"Энтропия: {entropy}")
print(f"Длина кода при равномерном кодировании: {math.log2(len(frequencies))}")
print(f"Избыточность: {redundancy}")

print_encoding(encoding)

# Кодируем и декодируем текст
encoded_text = encode_text(text, encoding)
decoded_text = decode_text(encoded_text, encoding)

print(f"\nИсходный текст: {text}")
print(f"Закодированный текст: {encoded_text}")
print(f"Декодированный текст: {decoded_text}")