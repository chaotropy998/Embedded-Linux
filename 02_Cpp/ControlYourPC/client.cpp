#include <arpa/inet.h>
#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string>

int main() {
    int clientSocket;
    struct sockaddr_in serverAddr;

    // Create a socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        perror("Error creating socket");
        return 1;
    }

    // Set up the server address structure
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1"); // Server IP address (localhost)
    serverAddr.sin_port = htons(8080); // Server port

    // Connect to the server
    if (connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("Error connecting to server");
        close(clientSocket);
        return 1;
    }

    std::cout << "Connected to the server." << std::endl;


    // Communication loop
    while (true) {
        std::cout << "Choose an option:" << std::endl;
        std::cout << "1. Open Firefox" << std::endl;
        std::cout << "2. Open Terminal" << std::endl;
        std::cout << "3. Send Notification" << std::endl;
        std::cout << "4. Open Calculator" << std::endl;
        std::cout << "Q. Quit" << std::endl;
        std::cout << "Enter your choice: ";

        char option;
        std::cin >> option;
        std::cin.ignore(); // Consume the newline character

        // Send the selected option to the server
        send(clientSocket, &option, sizeof(option), 0);

        if (option == 'Q' || option == 'q') {
            break; // Exit the loop and close the client
        }

        // Receive and display the response from the server
        char response[256];
        int bytesRead = recv(clientSocket, response, sizeof(response), 0);
        if (bytesRead <= 0) {
            std::cerr << "Server disconnected." << std::endl;
            break;
        }

    response[bytesRead] = '\0'; // Null-terminate the received data
    std::cout << "Server: " << response << std::endl;
}

    // Close the socket
    close(clientSocket);

    return 0;
}
