# Write your code below this line 👇

def prime_checker(number):
    count=0
    for i in range(1,number):
        if number%i==0:
            count+=1

    if count>1:
        print("not prime")
    else:
        print("prime")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)





# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")  
