#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

struct El{
    int valore;
    struct El *next;
};

int isEmpty(struct El *head){
    if(head == NULL)
        return 1;
    else
        return 0;
}

void enqueue(struct El **head, struct El **tail, struct El *element){
    if(isEmpty(*head))
        *head = element;
    else
        (*tail)->next = element;

    *tail = element;
    element->next = NULL;
}

struct El *dequeue(struct El **head, struct El **tail){
    struct El *ret = *head;

    if(isEmpty(*head)){
        return NULL;
    }else{
        *head = ret->next;
    }

    if(*head == NULL){
        *tail = NULL;
    } 
    
    return ret ;
}


int main(){
    char ancora ;
    struct El* head;
    struct El* tail;
    struct El* element;

    head = NULL ;
    tail = NULL ;

    do{
        element = (struct El*)malloc(sizeof(struct El));
        printf("\n");
        printf("Inserisci un numero:");
        fflush(stdin);
        scanf("%d", &element->valore);

        enqueue(&head, &tail, element);

        printf("Vuoi inserire un altro elemento? ");
        fflush(stdin);
        scanf("%c", &ancora);
    } while(ancora == 's');

    printf("\nLISTA: ");
    stampaLista(head);

    while(element != NULL){
        element = dequeue(&head, &tail);
        free(element);
    }

    printf("\nLISTA: ");
    stampaLista(head);
}