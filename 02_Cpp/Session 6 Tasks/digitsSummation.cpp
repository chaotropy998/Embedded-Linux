#include <iostream>
#include <string>

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    std:: string str = std::to_string(num);
    int sum = 0;
    for(char c : str) {
        sum += c - '0';
    }

    std::cout << "Sum of the given numbers is: " << sum << std::endl;
}