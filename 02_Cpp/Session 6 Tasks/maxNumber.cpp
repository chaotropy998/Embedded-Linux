#include <algorithm>
#include <iostream>


int main(){

    double num1, num2, num3;
    std::cout << "Enter the three numbers to compare between: " << std::endl;
    std::cin >> num1 >> num2 >> num3;
    std::cout << "The maximum number is: " << std::max({num1, num2, num3}) << std::endl;
}
