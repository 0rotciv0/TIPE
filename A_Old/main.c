#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>
#include <time.h>

struct tb { /*tableau de bits*/
    int* donnees;
    int taille;
};

typedef struct tb tb;

void free_tb(tb* t){
    free(t->donnees);
    free(t);
}

tb* tableau_aleatoire_bit(int n){
    srand(time(NULL));
    tb * tableau = malloc(sizeof(tb));
    tableau->taille = n;
    tableau->donnees = malloc(n*sizeof(int));

    for(int i = 0; i < n; i++){
        tableau->donnees[i] = rand() % 2;
    }
    return tableau;
}

void print_tableau(tb* t, int colonnes){
    if (t->taille == 0){return ;} 
    for(int i = 0; i < t->taille / colonnes; i++){
        for(int j = 0; j < colonnes; j++){
            printf("%i\t", t->donnees[i*colonnes + j]);
        }
        printf("\n");
        
    }
    for(int k = 0; k < t->taille % colonnes; k++){
        printf("%i\t", t->donnees[k]);
    }
    printf("\n");
}

void print_bool(bool b){
    if(b){printf("true");}
    else{printf("false");}
}

int log_2(int i){ return (int)(log10(i)/log10(2));}

tb* formatage(tb* t){ 
    int puissance_2 = log_2(t->taille);
    int nouv_taille  = t->taille + puissance_2 + 1;
    
    tb* nouv_t = malloc(sizeof(tb));
    nouv_t -> taille = nouv_taille;
    nouv_t -> donnees = malloc(sizeof(int)*nouv_taille);

    for(int i = 0; i < nouv_taille; i++){
        if (i==0){
            nouv_t -> donnees[i] = t -> donnees[0];
        }
        else{
            if ((i & (i - 1)) == 0){
                nouv_t -> donnees[i] = -1;
            }
            else { 
                nouv_t -> donnees[i] = t -> donnees[i-log_2(i)-1];
                // printf("case n°%i du tableau original ajouté !\n", i-log_2(i)-1);
            }
        }
    }

    free(t->donnees);
    free(t);
    return nouv_t;
}

void ajoute_correcteurs(tb* t){
    int pattern = 0b1;
    for(int i = 1; i < t->taille; i*=2){ 
        // on parcourt toutes les cases qui sont destinées aux codes correcteurs pour pouvoir les initialiser
        printf("\n\nLe bit correcteur placé en %i se base sur les cases :\t", i);
        int bit = 0b0;
        for(int j = 0; j < t->taille; j++){
            
            if ((j & pattern) != 0 && j != i) { 
                // Le premier test vérifie si les bits possèdent un 1 à la dernière place 
                // pour la première itération, puis l'avant dernière, etc

                // le second test permet de ne pas prendre en compte les bits correcteurs
                // qui sont arbitrairement initialisés à 0

                printf("%d ", j); // Affiche l'entier
                bit = bit ^ (t->donnees[j]);
            }
            
        }
        t->donnees[i] = bit;
        printf("\n\tBit correcteur placé en %i initialisé à %i\n", i, bit);
        pattern = pattern << 1;
    }
}

int verification(tb* t){
    int b = 0; 

    for(int i = 1; i < t->taille; i++){
        if(t->donnees[i] == 1 ){
            b = b ^ i;
        }
    }
    return b;
}

bool est_present(int* t, int taille, int k){
    for (int i = 0; i < taille; i++){
        if (t[i] == k){
            return true;
        }
    }
    return false;
} 

void ajout_erreur(tb* t, int nb_erreurs){
    int* indices = (int*)malloc(sizeof(int)*nb_erreurs);
    for(int i = 0; i < nb_erreurs; i++){

        int a_changer = rand()%(t->taille);
        while(est_present(indices, nb_erreurs, a_changer)){
            a_changer = rand()%(t->taille);
        }
        t->donnees[a_changer] = t->donnees[a_changer] ^ 1;
        indices[i] = a_changer;
        printf("Valeur en case n°%i changée\n", a_changer);
    }
    free(indices);
}





int main(){
    srand(time(NULL));
    int taille = 8;
    tb* tableau = tableau_aleatoire_bit(taille);

    printf("\n\n_____________________________________________________\n\n");

    printf("Tableau original :\n\n");
    print_tableau(tableau, ceil(sqrt(taille)));

    tb* nouv_t = formatage(tableau);

    ajoute_correcteurs(nouv_t);
    
    printf("\n\nTableau après modifications :\n\n");
    print_tableau(nouv_t, ceil(sqrt(taille) )); 
    // 'ceil' sert à faire un arrondi supérieur : si on a un tableau de 8 elem : on fait un tab 3x3 avec la case N-E vide

    printf("Résultat de la verif (0 si tout est conforme) : %i\n\n", verification(nouv_t));

    ajout_erreur(nouv_t, 2);

    print_tableau(nouv_t, ceil(sqrt(taille) ));

    free_tb(nouv_t);





    // printf("\n\n%i", ascii);


    printf("\n\n_____________________________________________________\n\n");
    
    return 0;
}


// nouv_t->donnees[9] = 1^(nouv_t->donnees[9]); // on créé volontairement une erreur sur la case 9
// nouv_t->donnees[12] = 1^(nouv_t->donnees[12]); // idem en 12


//stéganographie