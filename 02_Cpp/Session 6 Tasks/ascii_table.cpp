#include <iostream>

int main() {

    std::cout << "-----------------------" << std::endl;
    std::cout << "ASCII Table" << std::endl;
    std::cout << "-----------------------" << std::endl;
    std::cout << "Character  Decimal" << std::endl;
    std::cout << "-----------------------" << std::endl;

char ascii_char;
    for (int i = 32; i <= 126; ++i) {
        ascii_char = i;
        std::cout << "   " << ascii_char << "         " << i << std::endl;
    }
    return 0;
}