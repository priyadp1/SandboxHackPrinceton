#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int argc , char** argv){
   size_t size = 100000000000;
    char* p = malloc(size);
    if(!p){
        printf("Memory Allocation Failed\n");
        return 1;
    }
        memset(p, 1, size);
        printf("Memory Allocation Sucessful\n");
    return 0;
}