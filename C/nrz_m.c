/*
 Name : Vedang Kamat
 Roll No : 22B-ET-074
 Class : BE, SEM VII
 Branch : Electronics and Telecommunication Engineering
 Goa College of Engineering, Farmagudi
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function for NRZ-M encoding
void nrzm_encode(int *b, int n) {
    printf("NRZ-M: ");
    int current = 1;
    for (int i = 0; i < n; i++) {
        if (b[i] == 1) current = !current;
        printf(current ? "+V | " : "0 | ");
    }
    printf("\n");
}

int main() {
    char *input;   // pointer for input string
    int *b;        // dynamic array for bits
    int n;         // number of bits
    size_t max_len = 100; // maximum input length (can adjust)

    // Allocate memory for input string
    input = (char *)malloc((max_len + 1) * sizeof(char)); // +1 for null terminator
    if (input == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Input bit sequence as a string
    printf("Enter the bit sequence: ");
    scanf("%s", input);

    // Determine size automatically
    n = strlen(input);

    // Allocate memory for integer array
    b = (int *)malloc(n * sizeof(int));
    if (b == NULL) {
        printf("Memory allocation failed!\n");
        free(input);
        return 1;
    }

    // Convert string characters to integers
    for (int i = 0; i < n; i++) {
        if (input[i] == '0')
            b[i] = 0;
        else if (input[i] == '1')
            b[i] = 1;
        else {
            printf("Invalid character detected!\n");
            free(b);
            free(input);
            return 1;
        }
    }

    // Call NRZ-M encoding function
    nrzm_encode(b, n);

    // Free allocated memory
    free(b);
    free(input);
    return 0;
}

