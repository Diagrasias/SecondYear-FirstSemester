import string

# 1: Чтение зашифрованного текста из файла
with open('input.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# 2: Статистический анализ зашифрованного текста
def analyze_text(text):
    frequency = {}
    total_chars = 0

    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
            total_chars += 1

    for char in frequency:
        frequency[char] /= total_chars

    return frequency

encrypted_frequency = analyze_text(encrypted_text)

# 3: Статистические данные о вероятностном распределении символов русского языка
russian_language_frequency = {
    'а': 0.0801, 'б': 0.0159, 'в': 0.0454, 'г': 0.0170, 'д': 0.0298,
    'е': 0.0845, 'ж': 0.0094, 'з': 0.0165, 'и': 0.0735, 'й': 0.0121,
    'к': 0.0349, 'л': 0.0432, 'м': 0.0321, 'н': 0.0670, 'о': 0.1097,
    'п': 0.0281, 'р': 0.0473, 'с': 0.0547, 'т': 0.0626, 'у': 0.0262,
    'ф': 0.0026, 'х': 0.0097, 'ц': 0.0048, 'ч': 0.0144, 'ш': 0.0073,
    'щ': 0.0036, 'ъ': 0.0004, 'ы': 0.0190, 'ь': 0.0174, 'э': 0.0032,
    'ю': 0.0064, 'я': 0.0201
}

# 4: Восстановление исходного текста
def decrypt_text(encrypted_text, encrypted_frequency, language_frequency):
    decryption_key = {}

    encrypted_chars = sorted(encrypted_frequency.keys(), key=lambda x: encrypted_frequency[x], reverse=True)
    language_chars = sorted(language_frequency.keys(), key=lambda x: language_frequency[x], reverse=True)

    for i in range(len(encrypted_chars)):
        decryption_key[encrypted_chars[i]] = language_chars[i]

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_char = decryption_key.get(char, char)
        decrypted_text += decrypted_char

    return decrypted_text

decrypted_text = decrypt_text(encrypted_text, encrypted_frequency, russian_language_frequency)

# Итог:
print("Зашифрованный текст:")
print(encrypted_text)
print()
print("Восстановленный текст:")
print(decrypted_text)