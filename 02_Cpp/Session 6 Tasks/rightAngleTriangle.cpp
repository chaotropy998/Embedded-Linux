#include <iostream>

int main() {

    int base;

    std::cout << "Enter the triangle's base length:" << std::endl;
    std::cin >> base;

    for(int i = 1; i <= base; i++) {
        for(int j = 1; j <= i; j++) {
            std::cout << "*";
        }
        std:: cout << std::endl;
    }
}