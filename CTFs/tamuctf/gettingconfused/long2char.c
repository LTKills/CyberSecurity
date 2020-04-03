#include <stdio.h>

void printLong(unsigned long mylong) {
    int i;
    char* string = &mylong;

    for (i = 0; i < 8; i++) {
        printf("%c", string[i]);
    }

}


int main(){
    unsigned long mylong = (751367931562518887 & 0xff00000000000000) | 0xa706f6f6877;

    printLong(mylong);

    return 0;
}
