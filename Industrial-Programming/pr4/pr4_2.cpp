#include <iostream>
#include <cmath>

double nextFloat(int n) {
    return std::nextafter(n, INFINITY);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << "Наименьшее представимое число с плавающей точкой, следующее после " << n << " равно " << nextFloat(n) << std::endl;
    return 0;
}