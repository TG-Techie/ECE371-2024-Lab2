
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    x, y = 1, 0
    x_p, y_p = 0, 1
    a = e
    b = z
    
    while (b != 0):
        quotient = a // b
        a = b
        b = a % b

        x = x_p 
        x_p = x - quotient * x_p
        y = y_p
        y_p = y - quotient * y_p
    
    return x % z
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    else:
        n = p * q
        z = (p-1) * (q-1)
        
        e = 0
        while gcd(e,z) == 1: 
            e += 1

        d = get_d(e,z)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    e,n = pk
    asciiVal = ord(plaintext)
    cipher = (pow(asciiVal, e) % n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    d,n = pk
    decryptVal = (pow(ciphertext, d) % n)
    plain = chr(decryptVal)
    return ''.join(plain)

