import string

# Шаг 1: Предварительная обработка текста
def preprocess_text(text):
    text = text.lower()  # Приведение к нижнему регистру
    text = text.translate(str.maketrans("", "", string.punctuation))  # Удаление знаков препинания
    return text

# Шаг 2: Шифрование текста методом простой замены
def simple_substitution_encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            index = (alphabet.index(char) + key) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

def simple_substitution_decrypt(encrypted_text, key):
    return simple_substitution_encrypt(encrypted_text, -key)

# Шаг 3: Шифрование текста методом сложной замены
def complex_substitution_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = key.get(char, char)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def complex_substitution_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            decrypted_char = [k for k, v in key.items() if v == char]
            if decrypted_char:
                decrypted_text += decrypted_char[0]
            else:
                decrypted_text += char
        else:
            decrypted_text += char
    return decrypted_text

# Ну шо. Погнали
text = input("Введите текст: ")

# Шаг 1: Предварительная обработка текста
processed_text = preprocess_text(text)

# Шаг 2: Шифрование текста методом простой замены
key_simple = int(input("Введите ключ для простой замены: "))
encrypted_text_simple = simple_substitution_encrypt(processed_text, key_simple)
decrypted_text_simple = simple_substitution_decrypt(encrypted_text_simple, key_simple)

print("Зашифрованный текст (простая замена):", encrypted_text_simple)
print("Дешифрованный текст (простая замена):", decrypted_text_simple)

# Шаг 3: Шифрование текста методом сложной замены
key_complex = {}
for char in string.ascii_lowercase:
    encrypted_char = input("Введите зашифрованный символ для '{0}': ".format(char))
    key_complex[char] = encrypted_char
encrypted_text_complex = complex_substitution_encrypt(processed_text, key_complex)
decrypted_text_complex = complex_substitution_decrypt(encrypted_text_complex, key_complex)

print("Зашифрованный текст (сложная замена):", encrypted_text_complex)
print("Дешифрованный текст (сложная замена):", decrypted_text_complex)