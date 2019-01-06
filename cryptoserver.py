#def decipher(v, k):
#	y = v[0]
#	z = v[1]
#	delta = 0x9E3779B9
#	n=32
#	mySum = 0xC6EF3720
#	w=[0,0]
#	
#	while( n > 0 ):
#		z -= ( (y << 4) ) + k[2] ^ y + mySum ^ ( (y >> 5) ) + k[3]
#		y -= ( (z << 4) ) + k[0] ^ z + mySum ^ ( (z >> 5) ) + k[1]
#		mySum -= delta
 #       n -= 1
  #      y = (y & 0xffffffff)
   #     z = (z & 0xffffffff)
	#	
	#w[0] = bin(y)[2:]
	#w[1] = bin(z)[2:]
	#return w
from ctypes import *
	
def decipher(v, k):
    y=c_uint32(v[0])
    z=c_uint32(v[1])
    sum=c_uint32(0xC6EF3720)
    delta=0x9E3779B9
    n=32
    w=[0,0]

    while(n>0):
        z.value -= ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        y.value -= ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        sum.value -= delta
        n -= 1

    w[0]=bin(y.value)[2:]
    w[1]=bin(z.value)[2:]
    return w

import socket
import cPickle as pickle
import binascii
  
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

 
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
p = 1125899839733759
q = 4398042316799
n = p*q 
phiN = (p-1)*(q-1)
e = 3

d = modinv(e, phiN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
  
conn, addr = s.accept()
print 'Connection address:', addr

data = conn.recv(BUFFER_SIZE).decode()
if not data:
	print ("error")
else:
	print "received data:", data
conn.send(str(n)) 	
	
	
conn.close()

#TCP_IP = '127.0.0.1'
TCP_PORT1 = 5006
BUFFER_SIZE = 1024

  
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((TCP_IP, TCP_PORT1))
s1.send(str(e).encode("utf-8"))
Ciphertext = int(s1.recv(BUFFER_SIZE))

print ("Ciphertext: "), Ciphertext
print("")
Plaintext = pow(Ciphertext, d, n)
s1.send(str(Plaintext))


c1 = s1.recv(BUFFER_SIZE)
C1 = pickle.loads(c1)
c2 =s1.recv(BUFFER_SIZE)
C2 = pickle.loads(c2)
c3 = s1.recv(BUFFER_SIZE)
C3 = pickle.loads(c3)
c4 = s1.recv(BUFFER_SIZE)
C4 = pickle.loads(c4)
c5 = s1.recv(BUFFER_SIZE)
C5 = pickle.loads(c5)
c6 = s1.recv(BUFFER_SIZE)
C6 = pickle.loads(c6)
c7 = s1.recv(BUFFER_SIZE)
C7 = pickle.loads(c7)
c8 = s1.recv(BUFFER_SIZE)
C8 = pickle.loads(c8)
c9 = s1.recv(BUFFER_SIZE)
C9 = pickle.loads(c9)
c10 = s1.recv(BUFFER_SIZE)
C10 = pickle.loads(c10)
c11 = s1.recv(BUFFER_SIZE)
C11= pickle.loads(c11)
c12 = s1.recv(BUFFER_SIZE)
C12= pickle.loads(c12)
c13 = s1.recv(BUFFER_SIZE)
C13= pickle.loads(c13)

print("C1: "), C1
print("C2: "), C2
print("C3: "), C3
print("C4: "), C4
print("C5: "), C5
print("C6: "), C6
print("C7: "), C7
print("C8: "), C8
print("C9: "), C9
print("C10: "), C10
print("C11: "), C11
print("C12: "), C12
print("C13: "), C13

print("")
EncrK = s1.recv(BUFFER_SIZE)
EncryptedK = pickle.loads(EncrK)
print("EncryptedK: "), repr(EncryptedK)
print("")



k = []

k0=pow(EncryptedK[0], d, n)
k1=pow(EncryptedK[1], d, n)
k2=pow(EncryptedK[2], d, n)
k3=pow(EncryptedK[3], d, n)

k.append(int(k0))
k.append(int(k1))
k.append(int(k2))
k.append(int(k3))

print ("DecryptedK: "), k
print("")

import cPickle as pickle

InitialV = s1.recv(BUFFER_SIZE)

NewIVArray = pickle.loads(InitialV)
print("NewIVArray: "), repr(NewIVArray)

print("")

Cipher13 = []
Cipher13.append(int(C13[0]))
Cipher13.append(int(C13[1]))
Cipher12 = []
Cipher12.append(int(C12[0]))
Cipher12.append(int(C12[1]))

Decry13 = decipher(Cipher13, k)
print("Decry13: "), Decry13

P13 = []
p130 = int(Decry13[0], 2) ^ int(C12[0], 2)
p131 = int(Decry13[1], 2) ^ int(C12[1], 2)

P130 = '{0:b}'.format(p130)
P131 = '{0:b}'.format(p131)

P13.append(P130)
P13.append(P131)
print("P13: "), P13

##
Cipher12 = []
Cipher12.append(int(C12[0]))
Cipher12.append(int(C12[1]))
Cipher11 = []
Cipher11.append(int(C11[0]))
Cipher11.append(int(C11[1]))

Decry12 = decipher(Cipher12, k)
print("Decry12: "), Decry12

P12 = []
p120 = int(Decry12[0], 2) ^ int(C11[0], 2)
p121 = int(Decry12[1], 2) ^ int(C11[1], 2)

P120 = '{0:b}'.format(p120)
P121 = '{0:b}'.format(p121)

P12.append(P120)
P12.append(P121)
print("P12: "), P12

##
Cipher11 = []
Cipher11.append(int(C11[0]))
Cipher11.append(int(C11[1]))
Cipher10 = []
Cipher10.append(int(C10[0]))
Cipher10.append(int(C10[1]))

Decry11 = decipher(Cipher11, k)
print("Decry11: "), Decry11

P11 = []
p110 = int(Decry11[0], 2) ^ int(C10[0], 2)
p111 = int(Decry11[1], 2) ^ int(C10[1], 2)

P110 = '{0:b}'.format(p110)
P111 = '{0:b}'.format(p111)

P11.append(P110)
P11.append(P111)
print("P11: "), P11

##
Cipher10 = []
Cipher10.append(int(C10[0]))
Cipher10.append(int(C10[1]))
Cipher9 = []
Cipher9.append(int(C9[0]))
Cipher9.append(int(C9[1]))

Decry10 = decipher(Cipher10, k)
#print("Decry10: "), Decry10

P10 = []
p100 = int(Decry10[0], 2) ^ int(C9[0], 2)
p101 = int(Decry10[1], 2) ^ int(C9[1], 2)

P100 = '{0:b}'.format(p100)
P101 = '{0:b}'.format(p101)

P10.append(P100)
P10.append(P101)
#print("P10: "), P10

##
Cipher9 = []
Cipher9.append(int(C9[0]))
Cipher9.append(int(C9[1]))
Cipher8 = []
Cipher8.append(int(C8[0]))
Cipher8.append(int(C8[1]))

Decry9 = decipher(Cipher9, k)
#print("Decry9: "), Decry9

P9 = []
p90 = int(Decry9[0], 2) ^ int(C8[0], 2)
p91 = int(Decry9[1], 2) ^ int(C8[1], 2)

P90 = '{0:b}'.format(p90)
P91 = '{0:b}'.format(p91)

P9.append(P90)
P9.append(P91)
#print("P9: "), P9

##
Cipher8 = []
Cipher8.append(int(C8[0]))
Cipher8.append(int(C8[1]))
Cipher7 = []
Cipher7.append(int(C7[0]))
Cipher7.append(int(C7[1]))

Decry8 = decipher(Cipher8, k)
#print("Decry8: "), Decry8

P8 = []
p80 = int(Decry8[0], 2) ^ int(C7[0], 2)
p81 = int(Decry8[1], 2) ^ int(C7[1], 2)

P80 = '{0:b}'.format(p80)
P81 = '{0:b}'.format(p81)

P8.append(P80)
P8.append(P81)
#print("P8: "), P8

##
Cipher7 = []
Cipher7.append(int(C7[0]))
Cipher7.append(int(C7[1]))
Cipher6 = []
Cipher6.append(int(C6[0]))
Cipher6.append(int(C6[1]))

Decry7 = decipher(Cipher7, k)
#print("Decry7: "), Decry7

P7 = []
p70 = int(Decry7[0], 2) ^ int(C6[0], 2)
p71 = int(Decry7[1], 2) ^ int(C6[1], 2)

P70 = '{0:b}'.format(p70)
P71 = '{0:b}'.format(p71)

P7.append(P70)
P7.append(P71)
#print("P7: "), P7

##
Cipher6 = []
Cipher6.append(int(C6[0]))
Cipher6.append(int(C6[1]))
Cipher5 = []
Cipher5.append(int(C5[0]))
Cipher5.append(int(C5[1]))

Decry6 = decipher(Cipher6, k)
#print("Decry6: "), Decry6

P6 = []
p60 = int(Decry6[0], 2) ^ int(C5[0], 2)
p61 = int(Decry6[1], 2) ^ int(C5[1], 2)

P60 = '{0:b}'.format(p60)
P61 = '{0:b}'.format(p61)

P6.append(P60)
P6.append(P61)
#print("P6: "), P6

##
Cipher5 = []
Cipher5.append(int(C5[0]))
Cipher5.append(int(C5[1]))
Cipher4 = []
Cipher4.append(int(C4[0]))
Cipher4.append(int(C4[1]))

Decry5 = decipher(Cipher5, k)
#print("Decry5: "), Decry5

P5 = []
p50 = int(Decry5[0], 2) ^ int(C4[0], 2)
p51 = int(Decry5[1], 2) ^ int(C4[1], 2)

P50 = '{0:b}'.format(p50)
P51 = '{0:b}'.format(p51)

P5.append(P50)
P5.append(P51)
#print("P5: "), P5

##
Cipher4 = []
Cipher4.append(int(C4[0]))
Cipher4.append(int(C4[1]))
Cipher3 = []
Cipher3.append(int(C3[0]))
Cipher3.append(int(C3[1]))

Decry4 = decipher(Cipher4, k)
#print("Decry4: "), Decry4

P4 = []
p40 = int(Decry4[0], 2) ^ int(C3[0], 2)
p41 = int(Decry4[1], 2) ^ int(C3[1], 2)

P40 = '{0:b}'.format(p40)
P41 = '{0:b}'.format(p41)

P4.append(P40)
P4.append(P41)
#print("P4: "), P4

##
Cipher3 = []
Cipher3.append(int(C3[0]))
Cipher3.append(int(C3[1]))
Cipher2 = []
Cipher2.append(int(C2[0]))
Cipher2.append(int(C2[1]))

Decry3 = decipher(Cipher3, k)
#print("Decry3: "), Decry3

P3 = []
p30 = int(Decry3[0], 2) ^ int(C2[0], 2)
p31 = int(Decry3[1], 2) ^ int(C2[1], 2)

P30 = '{0:b}'.format(p30)
P31 = '{0:b}'.format(p31)

P3.append(P30)
P3.append(P31)
#print("P3: "), P3

##
Cipher2 = []
Cipher2.append(int(C2[0]))
Cipher2.append(int(C2[1]))
Cipher1 = []
Cipher1.append(int(C1[0]))
Cipher1.append(int(C1[1]))

Decry2 = decipher(Cipher2, k)
#print("Decry2: "), Decry2

P2 = []
p20 = int(Decry2[0], 2) ^ int(C1[0], 2)
p21 = int(Decry2[1], 2) ^ int(C1[1], 2)

P20 = '{0:b}'.format(p20)
P21 = '{0:b}'.format(p21)

P2.append(P20)
P2.append(P21)
#print("P2: "), P2

##
Cipher1 = []
Cipher1.append(int(C1[0]))
Cipher1.append(int(C1[1]))
Cipher0 = []
Cipher0.append(int(NewIVArray[0]))
Cipher0.append(int(NewIVArray[1]))

Decry1 = decipher(Cipher1, k)
#print("Decry1: "), Decry1

P1 = []
p10 = int(Decry1[0], 2) ^ int(NewIVArray[0], 2)
p11 = int(Decry1[1], 2) ^ int(NewIVArray[1], 2)

P10 = '{0:b}'.format(p10)
P11 = '{0:b}'.format(p11)

P1.append(P10)
P1.append(P11)
print("P1: "), P1

PlaintextConcat = P1[0] + P1[1] + P2[0] + P2[1] + P3[0] + P3[1] + P4[0] + P4[1] + P5[0] + P5[1] + P6[0] + P6[1] + P7[0] + P7[1] + P8[0] + P8[1] + P9[0] + P9[1] + P10[0] + P10[1] + P11[0] + P11[1] + P12[0] + P12[1] + P13[0] + P13[1]
#print("Decrypted value: "), PlaintextConcat
P1c = int('0b11000100101011000011000101111110',2)
P1char = binascii.unhexlify('%x' % P1c)
print("P1char: "),P1char
import hashlib
m = hashlib.md5()
m.update(PlaintextConcat)
print ("Sring Plaintext Digest: "), m.hexdigest()

s1.send(str(m.hexdigest()).encode())

s1.close()





