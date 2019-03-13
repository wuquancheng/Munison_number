import math 

def isPrime(n): 
  if n <= 1: 
      return 0
  i = 2
  while i*i <= n: 
      if n % i == 0: 
          return 0
      i += 1
  return 1

def monisen(No_monisen):
    counter_monisen = 0
    P_num = 1
    while counter_monisen != No_monisen :
        P_num = P_num+1
        P_isPrime = isPrime(P_num)
        if(P_isPrime == 1):
            M_num= math.pow(2,P_num) - 1
            M_num = int(M_num)
            M_isPrime = isPrime(M_num)
            if(M_isPrime == 1):
                if ( counter_monisen+1 ==No_monisen):
                    return(M_num)
                counter_monisen += 1

print(monisen(int(input()))) 
