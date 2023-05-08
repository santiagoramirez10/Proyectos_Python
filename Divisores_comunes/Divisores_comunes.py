# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""

def findDivisors(n1,n2):
    divisors=[]
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            divisors.append(i)
    return(divisors)
n1=90
n2=150
divisors=findDivisors(n1,n2)
print("los divisores comunes entre: "+str(n1)+" y "+str(n2))
for num in divisors:
    print(num)
