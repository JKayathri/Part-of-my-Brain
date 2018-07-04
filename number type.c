#include<stdio.h>
void main()
{
  int a;
  printf("\nEnter the value:");
  scanf("%d",&a);
  if(a<100000)
  {
     if(a>0)
        printf("\nPositive");
     else if(a<0)
        printf("\nNegative");
     else if(a==0)
        printf("\nZero");
     else
        printf("\nInvalid Input");
  }
}
