#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include<time.h>

int globalV = 0;

int aleatorio(){
    int num; 
    num = rand();
    return (num % 21) - 10;
}

void* funcionCambio(void* vargp)
{
    int num = aleatorio();
    globalV += num;
    printf("Numero generado: %i\n", num);
    printf("Valor de variable global: %d\n", globalV);

}

int main()
{
    srand(time(NULL)); 
    pthread_t thread_id;
    printf("Valor inicial de variable global: %d\n", globalV);
    for(int i=0;i<5;i++){
        pthread_create(&thread_id, NULL, funcionCambio, NULL);
    }
    pthread_join(thread_id, NULL);
    printf("\n***********************************************\n");
    printf("Valor final de variable global: %d\n", globalV);
    printf("***********************************************\n");
    pthread_exit(NULL);
}