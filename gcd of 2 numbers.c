#include"stdio.h"
int main()
{
  int a,b,num,i,flag;
  printf("\nEnter two numbers:\n");
  scanf("%d %d",&a,&b);
  if(a<b)
     num=a;
  else 
     num=b;
  for(i=num;i>=1;i--)
  {
     if((a%i==0) && (b%i==0))
        {
            printf("\nGCD of %d and %d is %d\n",a,b,i);
            flag=1;
        }
     if(flag==1)
         break;
    }
}
