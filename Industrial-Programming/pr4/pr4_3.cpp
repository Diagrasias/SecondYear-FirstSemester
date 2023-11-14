#include <ctime>
#include <iostream>

int getUTCDifference() {
    std::time_t t = std::time(nullptr);
    std::tm local = *std::localtime(&t);
    std::tm utc = *std::gmtime(&t);

    int localHour = local.tm_hour;
    int utcHour = utc.tm_hour;

    int diff = localHour - utcHour;

    // Если местное время находится в часовом поясе, отличном от UTC,
    // то разница может быть отрицательной. В этом случае мы добавляем 24,
    // чтобы получить положительное число.
    if (diff < 0) {
        diff += 24;
    }

    return diff;
}

int main() {
    std::cout << "Разница между местным временем и UTC составляет " << getUTCDifference() << " часов." << std::endl;
    return 0;
}