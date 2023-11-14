#include <iostream>

int getExponent(float num) {
    int exp = 0;
    float fractional = num;

    // Извлекаем целую часть числа
    while (fractional >= 1) {
        fractional /= 2;
        exp++;
    }

    // Двоичный поиск для поиска показателя степени
    int left = 0, right = exp, mid;
    while (left <= right) {
        mid = left + (right - left) / 2;
        float power = 1;
        for (int i = 0; i < mid; i++) {
            power *= 2;
        }
        if (power == num) {
            return mid;
        } else if (power < num) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    // Если число не является степенью двойки, возвращаем ближайшее к нему значение
    if (num - 1 < (right * right) - num) {
        return left;
    } else {
        return right;
    }
}

int main() {
    float num = 10.0;
    std::cout << "Показатель степени числа " << num << " равен " << getExponent(num) << std::endl;
    return 0;
}