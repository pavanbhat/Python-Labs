"""
Lab 4
This is an exercise from:
    http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html
that demonstrates how bitcoin mining works.  It performs only a single
pass of the SHA-256 algorithm to encrypt the first 32 bits of data.

Author: Sean Strout @ RIT CS
Author: <<< Pavan Prabhakar Bhat(pxb8715@rit.edu), Vinayak Marali(vkm7895@rit.edu)>>

Version: 1.1
"""

# constants
BITS = 32    # working with 32 bits of data

# the initial constants for SHA-256
A0 = 0x6a09e667
B0 = 0xbb67ae85
C0 = 0x3c6ef372
D0 = 0xa54ff53a
E0 = 0x510e527f
F0 = 0x9b05688c
G0 = 0x1f83d9ab
H0 = 0x5be0cd19
K = 0x428a2f98

def padIntTo32Bits(data):
    """
    Takes an integer that can be represented in 32 bits (or less), and returns
    it as a 32 bit binary string of 0's and 1's.], e.g.:

        padIntTo32Bits(11) = '0b00000000000000000000000000001011'
        padIntTo32Bits(0x6a09e667) = '0b01101010000010011110011001100111'

    :param data (int): An integer represented in 32 bits or less
    :pre: data is 32 bits or less
    :return: A 32 bit binary string
    """
    binaryValue = bin(data)[2:]
    size = len(binaryValue) # Caluculates the size of the data without "0b"
    zeroCount = BITS - size # Count of zeros to be padded
    str1 = "0b" + "0" * zeroCount + binaryValue[:]
    return str1

def Ma(A, B, C):
    """
    The Ma majority box looks at the bits of A, B, and C. For each position,
    if the majority of the bits are 0, it outputs 0. Otherwise it outputs 1.
    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param B (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param C (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string that stores the result
    """
    str1 = ""
    A,B,C = A[2:], B[2:], C[2:] # Removes the "0b" in the beginning
    for x in range(32):
        count = 0
        a = A[BITS-(x+1)] #Current bit from the string A
        b = B[BITS-(x+1)] #Current bit from the string B
        c = C[BITS-(x+1)] #Current bit from the string C
        if(a == "1"):
            count += 1
        if(b == "1"):
            count += 1
        if(c == "1"):
            count += 1
        if(count >= 2):
            str1 = "1" + str1 # appends the string if the majority is 1
        else:
            str1 = "0" + str1 # appends the string if the majority is 0
    str1 = "0b" + str1
    return str1


def rightShift(data, amount):
    """
    Right shift (rotating) a binary string by an amount, e.g.:

        rightShift('0b01101010000010011110011001100111', 2) ==
                   '0b11011010100000100111100110011001'

    This routine is used internally by Sum0() and Sum1() to
    perform the proper shifts.

    :param data (str): The 32 bit binary string to shift/rotate
    :param amount (int): The amount to shift/rotate
    :return: The resulting 32 bit binary string
    """
    # Removes the repetition of checks required for the amount of bits specified if greater than 32
    amount = amount % BITS
    if( amount == 0):
        str1 = "0b"+data[-(amount+1):] + data[2:-(amount+1)]
    else:
        str1 = "0b"+data[-amount:] + data[2:-amount]
    return str1

def Sum0(A):
    """
    Rotates the bits of A to form three rotated versions, and then sums them
    together modulo 2. In other words, if the number of 1 bits is odd, the sum
    is 1; otherwise, it is 0.  The three values in the sum are A rotated right
    by 2 bits, 13 bits, and 22 bits.

    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    sum1 = ""
    a = rightShift(A, 2)[2:]
    b = rightShift(A, 13)[2:]
    c = rightShift(A, 22)[2:]
    for x in range(BITS):
        # XOR operation on the bits done indirectly
        sum0 = int(a[x]) + int(b[(x)]) + int(c[x])
        sum0 %= 2
        sum1 = sum1 + str(sum0)
    sum1 = "0b" + sum1
    return sum1

def Ch(E, F, G):
    """
    The Ch "choose" box chooses output bits based on the value of input E. If
    a bit of E is 1, the output bit is the corresponding bit of F. If a bit
    of E is 0, the output bit is the corresponding bit of G. In this way, the
    bits of F and G are shuffled together based on the value of E.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param F (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param G (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    e = E[2:]
    f = F[2:]
    g = G[2:]
    ch = ""
    for x in range(BITS):
        if(e[x] == "1"):
           ch += f[x]
        else:
           ch += g[x]
    ch = "0b" + ch
    return ch

def Sum1(E):
    """
    This sum box rotates and sums the bits of E, similar to Sum0 except the
    shifts are 6, 11, and 25 bits.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    sum1 = ""
    a = rightShift(E, 6)[2:]
    b = rightShift(E, 11)[2:]
    c = rightShift(E, 25)[2:]
    for x in range(BITS):
        # XOR operation on the bits done indirectly
        sum0 = int(a[x]) + int(b[(x)]) + int(c[x])
        sum0 %= 2
        sum1 = sum1 + str(sum0)
    sum1 = "0b" + sum1
    return sum1

def trimTo32Bits(val):
    """
    Takes a binary string that may be larger than 32 bits and cut it down to 32
    bits by removing the extra most significant bits, e.g.:

        trim('0b111111110000010001000100001001101') ==
            '0b11111110000010001000100001001101'

    :param val (str): A binary string of 32 or greater bits
    :pre: val is >= 32 bits
    :return: A trimmed 32 bit binary string
    """
    val = val[2:]
    # Calculates the number of bits to be trimmed
    if(len(val) >= BITS):
        return "0b" + val[len(val)-BITS:]


def main():
    """
    The main performs a single pass of SHA-256 on a 32 bit user supplied input
    :return: None
    """

    # 1. Convert the initial values for A,B,C into padded binary strings
    A, B, C = padIntTo32Bits(A0), padIntTo32Bits(B0), padIntTo32Bits(C0)

    # 2. Compute the majority and sum0 boxes
    majority = Ma(A, B, C)
    print('Ma: bin=' + majority, ', hex=' + hex(int(majority, 2)))
    sum0 = Sum0(A)
    print('Sum0: bin=' + sum0 + ', hex=' + hex(int(sum0, 2)))

    # 3. Convert the initial values for E,F,G into padded binary strings
    E, F, G = padIntTo32Bits(E0), padIntTo32Bits(F0), padIntTo32Bits(G0)

    # 4. Compute the choose and sum1 boxes
    choose = Ch(E, F, G)
    print('Ch: bin=' + choose, ', hex=' + hex(int(choose, 2)))
    sum1 = Sum1(E)
    print('Sum1: bin=' + sum1, ', hex=' + hex(int(sum1, 2)))

    # 5. Prompt the user for a 32 bit integer, w, to encrypt
    w = int(input('Enter 32 bit input, e.g. 0x02000000:'), 16)

    # 6. Compute the overall sum
    sum = trimTo32Bits(bin(w + K + H0 + int(choose, 2) + int(sum1, 2)))
    print('sum: bin=' + sum, ', hex=' + hex(int(sum, 2)))

    # 7. Update to the new values for A-H
    newA = int(trimTo32Bits(bin(int(sum0, 2) + int(majority, 2) + int(sum,2))), 2)
    newB = int(A, 2)
    newC = int(B, 2)
    newD = int(C, 2)
    newE = int(trimTo32Bits(bin(D0 + int(sum,2))), 2)
    newF = int(E, 2)
    newG = int(F, 2)
    newH = int(G, 2)

    # display results
    print("newA:", hex(newA))
    print("newB:", hex(newB))
    print("newC:", hex(newC))
    print("newD:", hex(newD))
    print("newE:", hex(newE))
    print("newF:", hex(newF))
    print("newG:", hex(newG))
    print("newH:", hex(newH))

if __name__ == '__main__':
    main()