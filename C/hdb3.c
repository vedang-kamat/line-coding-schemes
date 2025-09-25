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

// Function for HDB3 encoding
void hdb3_encode(int *b, int n) {
    printf("HDB3: ");
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

int main() {
    char *input;
    int *b;
    int n;
    size_t max_len = 100;

    input = malloc((max_len + 1) * sizeof(char));
    if (!input) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the bit sequence: ");
    scanf("%100s", input);  // limit input to avoid overflow

    n = strlen(input);
    b = malloc(n * sizeof(int));
    if (!b) {
        printf("Memory allocation failed!\n");
        free(input);
        return 1;
    }

    for (int i = 0; i < n; i++) {
        if (input[i] == '0')
            b[i] = 0;
        else if (input[i] == '1')
            b[i] = 1;
        else {
            printf("Memory allocation failed!\n");
            free(b);
            free(input);
            return 1;
        }
    }

    hdb3_encode(b, n);

    free(b);
    free(input);
    return 0;
}

