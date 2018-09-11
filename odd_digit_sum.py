#include"stdio.h"
int main()
{
long int n;
int sum=0,rem;
printf("Enter n:\n");
scanf("%ld",&n);
while(n>0)
{
rem=n%10;
n=n/10;
if(rem%2!=0)
{
sum=sum+rem;
}
}
printf("\nSum of odd digits is %d\n",sum);
return 0;
}
