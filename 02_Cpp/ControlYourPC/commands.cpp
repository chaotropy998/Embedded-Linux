#include <cstring>
#include <iostream>
#include <cstdlib>

void openFirefox(){
    #ifdef _WIN32
    system("start firefox");
    
    #elif linux
    system("firefox &");
    #endif
}

void openCalculator(){
    #ifdef _WIN32
    system(" start calc");

    #elif linux
    system("gnome-calculator &");
    #endif
}