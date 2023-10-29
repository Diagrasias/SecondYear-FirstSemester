import math
from collections import Counter

def entropy(text):
    frequencies = Counter(text.lower())
    total_count = sum(frequencies.values())
    entropy = 0
    
    for frequency in frequencies.values():
        probability = frequency / total_count
        entropy -= probability * math.log2(probability)
    
    return entropy / total_count

def uniform_code_length(text):
    alphabet_size = len(set(text.lower()))
    code_length = math.ceil(math.log2(alphabet_size))
    redundancy = 1 - code_length / (math.log2(alphabet_size))
    
    return code_length, redundancy

def shannon_fano_code(text):
    frequencies = Counter(text.lower())
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    def recursive_encode(frequencies, code):
        if len(frequencies) == 1:
            return {frequencies[0][0]: code}
        
        split_index = len(frequencies) // 2
        left_symbols = [symbol for symbol, _ in frequencies[:split_index]]
        right_symbols = [symbol for symbol, _ in frequencies[split_index:]]
        
        left_code = recursive_encode(frequencies[:split_index], code + "0")
        right_code = recursive_encode(frequencies[split_index:], code + "1")
        
        return {**left_code, **right_code}
    
    code = recursive_encode(sorted_frequencies, "")
    return code

def average_code_length(text, code):
    total_count = sum(code.values())
    average_length = sum(len(code[symbol]) * frequency for symbol, frequency in Counter(text.lower()).items()) / total_count
    
    return average_length

def compression_efficiency(text, code):
    original_length = len(text) * 8 # assuming 8 bits per character
    compressed_length = sum(len(code[symbol]) for symbol in text.lower())
    efficiency = original_length / compressed_length
    
    return efficiency

def encode_text(text, code):
    encoded_text = ""
    for symbol in text.lower():
        encoded_text += code[symbol]
    
    return encoded_text

def decode_text(encoded_text, code):
    reversed_code = {value: key for key, value in code.items()}
    decoded_text = ""
    current_code = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_code:
            decoded_text += reversed_code[current_code]
            current_code = ""
    
    return decoded_text

# Задание 1
with open("input.txt", "r") as file:
    text = file.read()
    
    entropy_value = entropy(text)
    code_length, redundancy = uniform_code_length(text)
    
    print("Задание 1:")
    print(f"Энтропия текста: {entropy_value:.2f} бит/символ")
    print(f"Длина кода при равномерном кодировании: {code_length}")
    print(f"Избыточность: {redundancy:.2f}")

# Задание 2
code = shannon_fano_code(text)
    
print("\nЗадание 2:")
print("Схема алфавитного кодирования методом Шеннона-Фано:")
for symbol, symbol_code in code.items():
    print(f"{symbol}: {symbol_code}")

# Задание 3
average_length = average_code_length(text, code)
efficiency = compression_efficiency(text, code)
encoded_text = encode_text(text, code)
decoded_text = decode_text(encoded_text, code)

print("\nЗадание 3:")
print(f"Средняя длина элементарного кода: {average_length:.2f} бит/символ")
print(f"Эффективность сжатия: {efficiency:.2f}")
print(f"Закодированный текст: {encoded_text}")
print(f"Декодированный текст: {decoded_text}")