/*
 Name   : Vedang Kamat
 Roll No: 22B-ET-074
 Class  : BE, SEM VII
 Branch : Electronics and Telecommunication Engineering
 Goa College of Engineering, Farmagudi
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ================= Encoding Functions =================

// NRZ-L encoding
void nrzl_encode(int *b, int n) {
    printf("NRZ-L             : ");
    for (int i = 0; i < n; i++)
        printf(b[i] ? "+V | " : "0 | ");
    printf("\n");
}

// NRZ-M encoding
void nrzm_encode(int *b, int n) {
    printf("NRZ-M             : ");
    int current = 1;
    for (int i = 0; i < n; i++) {
        if (b[i] == 1) current = !current;
        printf(current ? "+V | " : "0 | ");
    }
    printf("\n");
}

// NRZ-S encoding
void nrzs_encode(int *b, int n) {
    printf("NRZ-S             : ");
    int current = 0;
    for (int i = 0; i < n; i++) {
        if (b[i] == 0) current = !current;
        printf(current ? "+V | " : "0 | ");
    }
    printf("\n");
}

// Manchester encoding
void manchester_encode(int *b, int n) {
    printf("Manchester        : ");
    for (int i = 0; i < n; i++) {
        int clk = 1;
        printf((!(b[i] ^ clk)) ? "+V " : "0 ");
        clk = 0;
        printf((!(b[i] ^ clk)) ? "+V | " : "0 | ");
    }
    printf("\n");
}

// Differential Manchester encoding
void diff_manchester_encode(int *b, int n) {
    printf("Diff Manchester   : ");
    int prev = 1;
    for (int i = 0; i < n; i++) {
        if (b[i] == 0) {
            prev = !prev;
            printf(prev ? "+V " : "0 ");
            prev = !prev;
            printf(prev ? "+V | " : "0 | ");
        } else {
            printf(prev ? "+V " : "0 ");
            prev = !prev;
            printf(prev ? "+V | " : "0 | ");
        }
    }
    printf("\n");
}

// Biphase-M encoding
void biphasem_encode(int *b, int n) {
    printf("Biphase-M         : ");
    int prev = 0;
    for (int i = 0; i < n; i++) {
        prev = !prev;
        printf(prev ? "+V " : "0 ");
        if (b[i] == 1) prev = !prev;
        printf(prev ? "+V | " : "0 | ");
    }
    printf("\n");
}

// Biphase-S encoding
void biphases_encode(int *b, int n) {
    printf("Biphase-S         : ");
    int prev = 0;
    for (int i = 0; i < n; i++) {
        prev = !prev;
        printf(prev ? "+V " : "0 ");
        if (b[i] == 0) prev = !prev;
        printf(prev ? "+V | " : "0 | ");
    }
    printf("\n");
}

// AMI encoding
void ami_encode(int *b, int n) {
    printf("AMI               : ");
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

// HDB3 encoding
void hdb3_encode(int *b, int n) {
    printf("HDB3              : ");
    int last_polarity = -1;
    int nonzero_count = 0;
    int zero_count = 0;

    for (int i = 0; i < n; i++) {
        if (b[i] == 1) {
            for (int z = 0; z < zero_count; z++) printf("0 | ");
            zero_count = 0;

            last_polarity = -last_polarity;
            printf(last_polarity == 1 ? "+V | " : "-V | ");
            nonzero_count++;
        } else {
            zero_count++;
            if (zero_count == 4) {
                if (nonzero_count % 2 == 0) {
                    printf("%s | 0 | 0 | %s | ",
                           last_polarity == -1 ? "+B" : "-B",
                           last_polarity == -1 ? "+V" : "-V");
                    last_polarity = -last_polarity;
                    nonzero_count += 2;
                } else {
                    printf("0 | 0 | 0 | %s | ", last_polarity == 1 ? "+V" : "-V");
                    nonzero_count++;
                }
                zero_count = 0;
            }
        }
    }

    for (int z = 0; z < zero_count; z++) printf("0 | ");
    printf("\n");
}

// B8ZS encoding
void B8ZS_encode(int *b, int n) {
    printf("B8ZS              : ");
    int last_polarity = -1;
    int zero_count = 0;

    for (int i = 0; i < n; i++) {
        if (b[i] == 1) {
            for (int z = 0; z < zero_count; z++) printf("0 | ");
            zero_count = 0;

            last_polarity = -last_polarity;
            printf(last_polarity == 1 ? "+V | " : "-V | ");
        } else {
            zero_count++;
            if (zero_count == 8) {
                if (last_polarity == 1)
                    printf("0 | 0 | 0 | +V | -B | 0 | -V | +B | "), last_polarity = +1;
                else
                    printf("0 | 0 | 0 | -V | +B | 0 | +V | -B | "), last_polarity = -1;
                zero_count = 0;
            }
        }
    }

    for (int z = 0; z < zero_count; z++) printf("0 ");
    printf("\n");
}

// Unipolar RZ encoding
void unipolar_rz(int *b, int n) {
    printf("Unipolar RZ       : ");
    for (int i = 0; i < n; i++) {
        if (b[i] == 1)
            printf("+V 0 | ");
        else
            printf("0 0 | ");
    }
    printf("\n");
}

// ================= Main Program =================

int main() {
    char *input;
    int *b, n;
    size_t max_len = 100;
    const char *default_bits = "100000000100001";  // default sequence

    input = malloc((max_len + 1) * sizeof(char));
    if (!input) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("\nEnter the bit sequence (default = %s): ", default_bits);
    if (!fgets(input, max_len, stdin)) {
        printf("Input error!\n");
        free(input);
        return 1;
    }

    // Remove trailing newline if present
    input[strcspn(input, "\n")] = '\0';

    // If input is empty, use default
    if (strlen(input) == 0) {
        strcpy(input, default_bits);
    }

    n = strlen(input);
    b = malloc(n * sizeof(int));
    if (!b) {
        printf("Memory allocation failed!\n");
        free(input);
        return 1;
    }

    for (int i = 0; i < n; i++) {
        if (input[i] == '0') b[i] = 0;
        else if (input[i] == '1') b[i] = 1;
        else {
            printf("Invalid character detected!\n");
            free(b);
            free(input);
            return 1;
        }
    }

    // Print all encodings
    printf("\n=== Line Coding Schemes ===\n");
    nrzl_encode(b, n);
    nrzm_encode(b, n);
    nrzs_encode(b, n);
    manchester_encode(b, n);
    diff_manchester_encode(b, n);
    biphasem_encode(b, n);
    biphases_encode(b, n);
    ami_encode(b, n);
    hdb3_encode(b, n);
    B8ZS_encode(b, n);
    unipolar_rz(b, n);

    free(b);
    free(input);
    printf("\n");
    return 0;
}


