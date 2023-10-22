#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string>
#include "commands.hpp"

int main() {
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t addrLen = sizeof(clientAddr);

    // Create a socket
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        perror("Error creating socket");
        return 1;
    }

    // Set up the server address structure
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8080);

    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("Error binding");
        close(serverSocket);
        return 1;
    }

    if (listen(serverSocket, 5) == -1) {
        perror("Error listening");
        close(serverSocket);
        return 1;
    }

    std::cout << "Server is listening on port 8080..." << std::endl;

    clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &addrLen);
    if (clientSocket == -1) {
        perror("Error accepting connection");
        close(serverSocket);
        return 1;
    }

    std::cout << "Client connected." << std::endl;

    // Communication loop
    while (true) {
    char option;
    char response[256];

    // Receive the selected option from the client
    int bytesRead = recv(clientSocket, &option, sizeof(option), 0);
    if (bytesRead <= 0) {
        std::cerr << "Client disconnected." << std::endl;
        break;
    }

    // Process the selected option
    switch (option) {
        case '1':
            openFirefox();
            strcpy(response, "Function 1 executed on the server.");
            break;

        case '2':
            // Execute function 2
            // You can add your logic here
            strcpy(response, "Function 2 executed on the server.");
            break;
        case '3':
            // Execute function 2
            // You can add your logic here
            strcpy(response, "Function 2 executed on the server.");
            break;
        case '4':
            openCalculator();
            strcpy(response, "Function 4 executed on the server.");
            break;

        default:
            // Handle invalid options
            strcpy(response, "Invalid option.");
            break;
    }

    // Send the response to the client
    send(clientSocket, response, strlen(response), 0);
    }

    // Close the sockets
    close(clientSocket);
    close(serverSocket);

    return 0;
}