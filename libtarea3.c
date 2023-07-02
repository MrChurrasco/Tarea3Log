#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

// Metodos para hacer Hashing
unsigned long long int siguiente_primo(unsigned long long int num) {
    num++;
    if (num <= 2) {
        return 2;
    }
    if ((num & 1) == 0) {
        num++;
    }
    while (true) {
        bool es_primo = true;
        unsigned long long int raiz = sqrt(num);
        for (unsigned long long int i = 3; i <= raiz; i += 2) {
            if (num % i == 0) {
                es_primo = false;
                break;
            }
        }
        if (es_primo) {
            return num;
        }
        num += 2;
    }
}

unsigned long long int funcion_hash(unsigned long long int a, unsigned long long int b, unsigned long long int p, unsigned long long int m, unsigned long long int x) {
    return ((a*x + b) % p) % m;
}