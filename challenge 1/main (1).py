# Implement a recursive function to calculate the factorial of a given number
'''
formula n!=n*(n-1)
10!= 10*9!
2!= 2*1
3!= 3*2!

'''


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)
    
number = int(input("enter the value:"))
res = fact_rec(number)
print("The factoril of {} is {}".format(number, res))
