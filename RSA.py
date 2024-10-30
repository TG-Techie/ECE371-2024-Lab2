import random


# function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    assert 0 != a
    assert 0 != b

    while b != 0:
        a, b = b, a % b
    return a


# uses extened euclidean algorithm to get the d value
def get_d(e, z):
    # HAVEDONE
    ###################################your code goes here#####################################

    # use the euclidian algorithm where
    #  a*x + b*y = gcd(a,b)

    assert 1 == gcd(e, z)

    x, y = 1, 0
    x_p, y_p = 0, 1  # x' and y' , the next values
    a = e
    b = z

    while b != 0:
        quotient = a // b
        (a, b) = (b, a % b)

        (x, x_p) = (x_p, x - quotient * x_p)
        (y, y_p) = (y_p, y - quotient * y_p)

    return x % z


def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
            else:
                return True

    else:
        return False


def are_relatively_prime(a: int, b: int) -> bool:
    return 1 == gcd(a, b)


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    # HAVEDONE
    ###################################your code goes here#####################################

    n = p * q
    z = (p - 1) * (q - 1)

    for maybe_e in range(n - 1, 0 - 1, -1):
        if not are_relatively_prime(maybe_e, z):
            continue
        e = maybe_e
        break
    else:
        raise ValueError(f"could not find an e < n where {n=}")

    d = get_d(e, z)

    assert d != n
    assert e != n
    assert d != e

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # HAVEDONE
    ###################################your code goes here#####################################
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    e, n = pk
    asciiVal = ord(plaintext)
    cipher = pow(asciiVal, e) % n
    return cipher


def decrypt(pk, ciphertext):
    # HAVEDONE
    ###################################your code goes here#####################################
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext
    d, n = pk
    decryptVal = pow(ciphertext, d) % n
    plain = chr(decryptVal)
    return "".join(plain)
