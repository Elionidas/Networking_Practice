//this is a test to turn c++ code into assembly through the use of GCC and the g++ compiler

#include <stdio.h>
//global string
char s[] = "Test string";

//driver code
int main()
{
    //declare variable
    int a = 2000, b = 17;
    
    //printing statement
    printf ("%s %d \n", s, a+b);
}