#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct Tnode{
    int data;
    struct Tnode *left;
    struct Tnode *right;

}Tnode;

int main(){
    int strong;
    Tnode *A, *B, *C, *D, *E;
    A = (Tnode*)malloc(sizeof(Tnode));
    B = (Tnode*)malloc(sizeof(Tnode));
    C = (Tnode*)malloc(sizeof(Tnode));
    D = (Tnode*)malloc(sizeof(Tnode));
    E = (Tnode*)malloc(sizeof(Tnode));

    printf("추가 강화 수치 입력 >>");
    scanf("%d", &strong);
    

    A->data = 10;
    A->left = B;
    A->right = C;

    B->data = 20;
    B->left = D;
    B->right = NULL;

    C->data = 15;
    C->left = E;
    C->right = NULL;

    D->data = 40+strong;
    D->left = NULL;
    D->right = NULL;

    E->data = 35;
    E->left = NULL;
    E->right = NULL;

    // printf("%d\n", A->data);
    // printf("%d\n", B->data);
    // printf("%d\n", C->data);
    // printf("%d\n", D->data);
    // printf("%d\n", E->data);

    printf("%d\n", A->data+B->data+D->data);

    return 0;
}