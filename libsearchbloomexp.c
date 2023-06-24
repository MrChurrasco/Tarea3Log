#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

// Genera una función hash que toma un valor como entrada y devuelve un valor hash en módulo M
unsigned int hash_function(char *value, int m) {
    static int seed = 0; // Inicializa una variable estática para llevar la semilla de la función hash
    unsigned char hash[SHA256_DIGEST_LENGTH]; // Asigna un array para almacenar el valor hash
    char seed_str[16];
    sprintf(seed_str, "%d", seed); // Convierte la semilla en una cadena
    seed++; // Incrementa la semilla
    char *data = malloc(strlen(seed_str) + strlen(value) + 1); // Asigna una nueva cadena para almacenar la semilla y la cadena de entrada
    strcpy(data, seed_str); // Copia la semilla en la nueva cadena
    strcat(data, value); // Concatena la cadena de entrada en la nueva cadena
    SHA256(data, strlen(data), hash); // Calcula el valor hash SHA-256 de la nueva cadena
    free(data); // Libera la memoria utilizada por la nueva cadena
    return *(unsigned int*)hash % m; // Devuelve los primeros 4 bytes del valor hash como un entero sin signo módulo m
}



