#include <iostream>
#include <regex>

int main() {
    std::regex email_regex("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}");
    std::regex url_regex("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+");

    std::string email = "example@gmail.com";
    std::string url = "https://www.google.com";

    if (std::regex_match(email, email_regex)) {
        std::cout << "Email is valid" << std::endl;
    } else {
        std::cout << "Email is not valid" << std::endl;
    }

    if (std::regex_match(url, url_regex)) {
        std::cout << "URL is valid" << std::endl;
    } else {
        std::cout << "URL is not valid" << std::endl;
    }

    return 0;
}