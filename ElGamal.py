def egcd(a, m):
    if a==0:
        return (m, 0, 1)
    else:
        g, y, x = egcd(m%a, a)
        return (g, x-(m//a)*y, y)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1:
        print("Modular inverse does not exist!")
    else:
        return x%m
    
def inverseMod(a, m):

    for i in range(1,m):

        if ( m*i + 1) % a == 0:

            return ( m*i + 1) // a

    return None
print ('This is a program to illustrate ElGamal key generation, encryption, decrption, signing and verification')
print("")
p = 3000273817
g = 23

a = 357689045

Alpha = pow(g,a,p)
print("Alice's public key is %s" % (Alpha))
print("Her private key is %s" % (a))
print('Key generation done')
print("")

Plaintext = 21873451
k = 5
u = pow(g,k,p)
d = pow(Alpha,k,p)
Ciphertext = (Plaintext*d)% p
print("The Encrypted text is %s" % (Ciphertext))
print ("End of encryption")
print("")

inv = modinv(pow(u,a,p), p)
print ("The inverse is %s" % (inv))
Decrypt = (Ciphertext*inv) % p
print ("The decrypted message is %s" % (Decrypt))
print ('End of decryption')
print("")

M = 12908142
kinv = modinv(k, p-1)
print("The inverse of k (%s) mod p-1(%s) is %s" % (k, p-1, kinv))
S = ((M - (a*u))*kinv) % (p-1)
print ("The signed message is %s" % (S))
print ('End of signing')
print("")
bb = pow(Alpha,u,p)
cc = pow(u,S,p)
Ver = (bb*cc) % p
print("The verified message is %s" % Ver)

print (pow(g,M,p))


