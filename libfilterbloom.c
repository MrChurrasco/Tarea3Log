#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

int search_string(char **array, int length, char *string) {
    int i;
    for (i = 0; i < length; i++) {
        if (strcmp(array[i], string) == 0) {
            return 1;
        }
    }
    return 0;
}


