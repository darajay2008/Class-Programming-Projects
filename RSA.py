


def inverseMod(a, m):

    for i in range(1,m):

        if ( m*i + 1) % a == 0:

            return ( m*i + 1) // a

    return None


print ('This is a program to illustrate RSA key generation, encryption, decrption, signing and verification')
print("")
p = 7919
q= 7589

n = p*q
phiN = (p-1)*(q-1)
e = 3

d = inverseMod(e, phiN)
print ("Euler totient for n=pq is:")
print(phiN)
print("")
print("The Modular multiplicative inverse of %s modulo phiN %s is %s" % (e, phiN, d))
print ("Key pair generation done: the encryption exponent is %s and the decryption exponent is %s " % (e, d))
print('')

Plaintext = 1234567

Ciphertext= pow(Plaintext,e,n)

print ("The ciphertext is %s" % (Ciphertext))
print ('Encryption done')
print("")

DecryptedPlaintext = pow(Ciphertext,d,n)

print ("The decrypted plaintext is %s" % (DecryptedPlaintext))
print ('Decryption done')
print("")

dig = 12378345


print("The private key is %s" % d)
S = pow(dig,d,n)
print ("The signed digest is %s" % (S))
print ('End of signing')
print("")

print("The public key is %s" % e)
M = pow(S,e,n)
print ("The verified digest is %s" % (M))
print ('End of verification')



