#include <stdlib.h>
#include <stdio.h>



int main() {
    char **vec1 = malloc(sizeof(char*));
    vec1[0] = malloc(sizeof(char));
    vec1[0][0] = (char)123;
    printf("%d %d\n", *vec1[0], vec1[0][0]);
    return 0;
}
