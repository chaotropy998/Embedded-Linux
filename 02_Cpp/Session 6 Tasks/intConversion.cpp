#include <iostream>
#include <bitset>
#include <string>

void decimalToBinary(int decimalNumber){
    int numBits = 0;
    int k = decimalNumber;
    while (k > 0) {
        numBits++;
        k >>= 1; 
    }

    std::bitset<64> binaryValue(decimalNumber);
    std:: cout << "Binary number for " << decimalNumber << " is: " << binaryValue.to_string().substr(64 - numBits) << std::endl;
}

void binaryToDecimal(std::string binaryNumber){
    std::bitset<64> bits(binaryNumber);

    unsigned long decimalValue = bits.to_ullong();
    std:: cout << "Decimal number for " << binaryNumber << " is: " << decimalValue << std::endl;
}

int main() {
    int decimalNumber;
    std::cout << "Enter a decimal number: ";
    std::cin >> decimalNumber;
    decimalToBinary(decimalNumber);

    std::string binaryNumber;
    std::cout << "Enter a binary number: ";
    std::cin >> binaryNumber;
    binaryToDecimal(binaryNumber);
}