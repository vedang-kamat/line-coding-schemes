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

// Function for Biphase-M encoding
void biphasem_encode(int *b, int n) {
    printf("Biphase-M: ");
    int prev = 0;
    for (int i = 0; i < n; i++) {
        prev = !prev;
        printf(prev ? "+V " : "0 ");
        if (b[i] == 1) prev = !prev;
        printf(prev ? "+V | " : "0 | ");
    }
    printf("\n");
}

int main() {
    char *input;        // bitstream string
    int *b;             // bit array
    int n;              // number of bits
    size_t max_len = 100;

    // Allocate memory for input string
    input = (char *)malloc((max_len + 1) * sizeof(char));
    if (input == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Input bit sequence
    printf("Enter the bit sequence: ");
    scanf("%s", input);

    // Number of bits
    n = strlen(input);

    // Allocate memory for bits
    b = (int *)malloc(n * sizeof(int));
    if (b == NULL) {
        printf("Memory allocation failed!\n");
        free(input);
        return 1;
    }

    // Convert input string to bit array
    for (int i = 0; i < n; i++) {
        if (input[i] == '0') {
            b[i] = 0;
        } else if (input[i] == '1') {
            b[i] = 1;
        } else {
            printf("Invalid character detected!\n");
            free(b);
            free(input);
            return 1;
        }
    }

    // Encode
    biphasem_encode(b, n);

    free(b);
    free(input);
    return 0;
}

