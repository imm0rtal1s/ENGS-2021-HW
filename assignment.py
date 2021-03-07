def nthfibonacci(age):
       if(age <= 100 and age >=2):
            n1 = 0
            n2 = 1
            sum = 0
            while (n2 <= age):
               sum = n2 + sum
               temp = n1 + n2
               n1 = n2
               n2 = temp
            print(sum)
            return sum
       else:
        print("Please enter your age")
        return 1

def isprime(ans):
    for i in range(2,int(ans**0.55)+1):
       if ans%i==0:
           print("your age is not prime")
           return False

    print("your age is prime")
    return True

def tobinary(age):
   binary = [0,0,0,0,0,0,0,0]
   i = len(binary)-1
   while(age > 0):
       binary[i] = age%2
       i-=1
       age = int(age/2)
   print(binary)

def main():
       while (True):
           N = int(input("enter your age: "))
           if(nthfibonacci(N) != 1):
               isprime(N)
               tobinary(N)
               print("Thank you, Goodbye")
               break

main()

