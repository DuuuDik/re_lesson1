'''
Напишите функцию, вычисляющую число Фибоначчи по его порядковому номеру.
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
'''

n = 0 
calculated_value = 0
F_values = {n: calculated_value}

def fib(n: int) -> int:
  if n==0 or n==1:
    return n
  elif n in F_values:
    return F_values[n]
  else:
    calculated_value=fib(n-1)+fib(n-2)
    F_values[n] = calculated_value
    return calculated_value
    
print(fib(5))