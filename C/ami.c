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

// Function for AMI encoding
void ami_encode(int *b, int n) {
    printf("AMI: ");
    int prev = 0;
    for (int i = 0; i < n; i++) {
        if (b[i] == 1) {
            prev = !prev;
            printf(prev ? "+V | " : "-V | ");
        } else {
            printf("0 | ");
        }
    }
    printf("\n");
}

int main() {
    char *input;    // input bitstream as string
    int *b;         // bit array
    int n;          // number of bits
    size_t max_len = 100;

    // Allocate memory for input string
    input = (char *)malloc((max_len + 1) * sizeof(char));
    if (input == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Read bit sequence
    printf("Enter the bit sequence: ");
    scanf("%s", input);

    // Determine number of bits
    n = strlen(input);

    // Allocate memory for bit array
    b = (int *)malloc(n * sizeof(int));
    if (b == NULL) {
        printf("Memory allocation failed!\n");
        free(input);
        return 1;
    }

    // Convert string to int array
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

    // Perform AMI encoding
    ami_encode(b, n);

    // Free memory
    free(b);
    free(input);

    return 0;
}

