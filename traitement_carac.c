#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>
#include <time.h>


// unsigned char carac = 200;

// int ascii_code = (int)carac;

// printf("\n\n%c", ascii_code);



// unsigned char c = 'A';

// int ascii = (int) c;


int charac_to_ascii(unsigned char c){
    return (int) c;
}

int* dec_to_binary_8(int n){
    int* binaire = (char*)malloc(sizeof(int) * 8); // on code sur 8 bits
    for(int i = 7; i >= 0; i++){
        if(n / (2^i)){
            
        }
    }

}


int main(){
    printf("Code Ascii de 'A' : %i", charac_to_ascii('A'));

    return 0;
}