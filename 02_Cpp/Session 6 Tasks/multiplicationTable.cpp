#include <iostream>
#include <iomanip>

int main() {

    std::cout << "Number ";
    for (int i = 1; i <= 12; i++) {
        std::cout << std::setw(5) << i;
    }
    std::cout << std::endl;

    for (int number = 1; number <= 12; number++) {
        std::cout << std::setw(5) << number << " |";

        for (int i = 1; i <= 12; i++) {
            std::cout << std::setw(5) << (number * i);
        }

        std::cout << std::endl;
    }

    return 0;
}
