start = 1
end = 10000
primes=[]
for val in range(start, end + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           primes.append(val)
print(primes)
