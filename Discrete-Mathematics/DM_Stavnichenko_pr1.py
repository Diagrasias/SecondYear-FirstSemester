import string
import math
from collections import Counter

# Чтение текста из файла
def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Приведение слов к нижнему регистру, удаление знаков препинания и пробелов
def process_text(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation + ' '))
    return text

# Сохранение обработанного текста в файл
def save_text(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

# Подсчет частоты появления однобуквенных и двухбуквенных сочетаний
def count_combinations(text):
    single_letters = Counter(text)
    double_letters = Counter(text[i:i+2] for i in range(len(text)-1))
    return single_letters, double_letters

# Подсчет энтропии для однобуквенных и двухбуквенных сочетаний
def calculate_entropy(combinations):
    total_count = sum(combinations.values())
    entropy = sum(-count/total_count * math.log2(count/total_count) for count in combinations.values())
    return entropy

# Подсчет длины кода при равномерном побуквенном кодировании и избыточности
def calculate_code_length(combinations):
    total_count = sum(combinations.values())
    code_length = math.log2(total_count)
    redundancy = code_length - math.log2(len(combinations))
    return code_length, redundancy

# Удаление 20% наиболее или редко встречающихся символов
def remove_characters(text, percentage, most_common):
    characters_count = Counter(text)
    total_count = sum(characters_count.values())
    if most_common:
        characters_count = characters_count.most_common(int(percentage * total_count))
    else:
        characters_count = characters_count.most_common()[:-int(percentage * total_count)]
    characters = set(character for character, _ in characters_count)
    text_without_characters = ''.join(character for character in text if character in characters)
    return text_without_characters

# Пример использования

# 1. Чтение текста из файла
text = read_text('input.txt')

# 2. Приведение слов к нижнему регистру, удаление знаков препинания и пробелов
processed_text = process_text(text)

# 3. Подсчет частоты появления однобуквенных и двухбуквенных сочетаний
single_letters, double_letters = count_combinations(processed_text)

# 4. Подсчет энтропии для однобуквенных и двухбуквенных сочетаний
entropy_single_letters = calculate_entropy(single_letters)
entropy_double_letters = calculate_entropy(double_letters)

# 5. Подсчет длины кода при равномерном побуквенном кодировании и избыточности
code_length, redundancy = calculate_code_length(single_letters)

# 6. Удаление 20% наиболее часто встречающихся символов
text_without_most_common = remove_characters(processed_text, 0.2, True)
single_letters_without_most_common, _ = count_combinations(text_without_most_common)
entropy_single_letters_without_most_common = calculate_entropy(single_letters_without_most_common)

# 7. Удаление 20% наиболее редко встречающихся символов
text_without_least_common = remove_characters(processed_text, 0.2, False)
single_letters_without_least_common, _ = count_combinations(text_without_least_common)
entropy_single_letters_without_least_common = calculate_entropy(single_letters_without_least_common)

# Сохранение результата
save_text(processed_text, 'processed_text.txt')
save_text(str(entropy_single_letters), 'entropy_single_letters.txt')
save_text(str(entropy_double_letters), 'entropy_double_letters.txt')
save_text(str(code_length), 'code_length.txt')
save_text(str(redundancy), 'redundancy.txt')
save_text(str(entropy_single_letters_without_most_common), 'entropy_single_letters_without_most_common.txt')
save_text(str(entropy_single_letters_without_least_common), 'entropy_single_letters_without_least_common.txt')