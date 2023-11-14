#include <iostream>
#include <string>
#include <regex>

std::string cleanPhoneNumber(const std::string& phoneNumber) {
    std::regex regex("\\D");
    std::string cleanedNumber = std::regex_replace(phoneNumber, regex, "");
    return cleanedNumber;
}

std::string cleanCardNumber(const std::string& cardNumber) {
    std::regex regex("\\D");
    std::string cleanedNumber = std::regex_replace(cardNumber, regex, "");
    return cleanedNumber;
}

int main() {
    std::string phoneNumber = "+1 (123) 456-7890";
    std::string cardNumber = "1234 5678 9012 3456";

    std::string cleanedPhoneNumber = cleanPhoneNumber(phoneNumber);
    std::string cleanedCardNumber = cleanCardNumber(cardNumber);

    std::cout << "Cleaned Phone Number: " << cleanedPhoneNumber << std::endl;
    std::cout << "Cleaned Card Number: " << cleanedCardNumber << std::endl;

    return 0;
}