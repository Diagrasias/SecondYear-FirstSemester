#include <regex>
#include <string>
#include <iostream>
#include <fstream>
#include <streambuf>

int main() {
    std::ifstream file("index.html");
    std::string html((std::istreambuf_iterator<char>(file)),
                      std::istreambuf_iterator<char>());

    std::regex imgRegex(R"|(<img[^>]+src\s*=\s*['"]([^'"]+)['"][^>]*>)|");
    std::sregex_iterator it(html.begin(), html.end(), imgRegex), end;

    for (; it != end; ++it) {
        std::cout << "Image URL: " << it->str(1) << std::endl;
    }

    return 0;
}