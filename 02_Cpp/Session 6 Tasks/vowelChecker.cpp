#include <cctype>
#include <iostream>

bool isVowel(char character){
    character = tolower(character);
    char vowels[] = {'a','e','i','o','u'};
    for(int i = 0; i < sizeof(vowels) / sizeof(vowels[0]); i++){
        if(character == vowels[i]){
            return true;
        }
    }
    return false;
}

int main(){
    char character;
    std::cout << "Enter a character: ";
    std::cin >> character;

    if(isVowel(character)){
        std::cout << character << " is a vowel." << std::endl;
    }
    else{
        std::cout << character << " is not a vowel." << std::endl;
    }
    return 0;
}