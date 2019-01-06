from ctypes import *

def encipher(v, k):
    y=c_uint32(v[0]);
    z=c_uint32(v[1]);
    sum=c_uint32(0);
    delta=0x9E3779B9;
    n=32
    w=[0,0]

    while(n>0):
        sum.value += delta
        y.value += ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        z.value += ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        n -= 1

    w[0]=bin(y.value)[2:]
    w[1]=bin(z.value)[2:]
    return w





import socket
import cPickle as pickle
  
  
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello"
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
n = int(s.recv(BUFFER_SIZE))

s.close()
  
print "modulus n:", n

#TCP_IP1 = '127.0.0.1'
TCP_PORT1 = 5006
BUFFER_SIZE1 = 20


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((TCP_IP, TCP_PORT1))
s1.listen(1)



conn, addr = s1.accept()
print 'Connection address:', addr

e = int(conn.recv(BUFFER_SIZE1).decode("utf-8"))
if not e:
	print ("error")
else:
	print "encryption exponent:", e
#conn.send(str(n)) 	"""
#print e

from random import randint
x = randint (100000000000000000000000, 999999999999999999999999)
print ("x: "), x
Ciphertext= pow(x,e,n)

conn.send(str(Ciphertext))
Plaintext = int(conn.recv(BUFFER_SIZE))
print ("Plaintext: "), Plaintext
print("")
string_plaintext = "a" *100

#print ("String Plaintext: "), string_plaintext
#print  ("plaintext to int: "), ord("a")
print("")
plaintextArray = []
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("aaaa")
plaintextArray.append("0000")

#print ("Plaintext array text [0]: "), plaintextArray[0]

plaintextConcat = plaintextArray[0] + plaintextArray[1] + plaintextArray[2] + plaintextArray[3] + plaintextArray[4] + plaintextArray[5] + plaintextArray[6] + plaintextArray[7] + plaintextArray[8] + plaintextArray[9] + plaintextArray[10] + plaintextArray[11] + plaintextArray[12] + plaintextArray[13] + plaintextArray[14] + plaintextArray[15] + plaintextArray[16] + plaintextArray[17] + plaintextArray[18] + plaintextArray[19] + plaintextArray[20] + plaintextArray[21] + plaintextArray[22] + plaintextArray[23] + plaintextArray[24] + plaintextArray[25]

print ("Plaintext Concat: "), plaintextConcat
print("")

import hashlib
m = hashlib.md5()
m.update(plaintextConcat)
print ("Sring Plaintext Digest: "), m.hexdigest()
import binascii
import uuid

k = []

k1 = (bin(uuid.uuid4().int & (1<<32)-1))[2:]
k2 = (bin(uuid.uuid4().int & (1<<32)-1))[2:]
k3 = (bin(uuid.uuid4().int & (1<<32)-1))[2:]
k4 = (bin(uuid.uuid4().int & (1<<32)-1))[2:]

k.append(int(k1 , 2))
k.append(int(k2 , 2))
k.append(int(k3 , 2))
k.append(int(k4 , 2))
#uuid.uuid4()
print("")
print ("Random key K: "), k
print("")

#print ("Length of key[0]: "), len(k[0])

#IV = format (0, '010b')
#IV = "0" *8
IVArray = []

IVArray.append("0000")
IVArray.append("0000")
IV0 = bin(int(binascii.hexlify(IVArray[0]), 16))[2:]
IV1 = bin(int(binascii.hexlify(IVArray[1]), 16))[2:]

NewIVArray = []
NewIVArray.append(IV0)
NewIVArray.append(IV1)
print ("New IV Array: "), NewIVArray

print("")
#print("IV1: "), IVArray[1]
plaintextBinary = []

for i in range(0, 26):
	w = bin(int(binascii.hexlify(plaintextArray[i]), 16))[2:]
	plaintextBinary.append(w)
	
#plaintextBinary = bin(int(binascii.hexlify(plaintextArray[0]), 16))
print("PlaintextBinary: "), plaintextBinary
print("")
print ("Length of Plaintext[0]: ")
print(len(plaintextBinary[0]))
print("")
print ("Length of IV[0]: "), len(NewIVArray[0])
print("")

result = NewIVArray
q = 1
CiphertextArray = []

for j in range (0, 26, 2):
	PTArray = []
	PTArray.append(plaintextBinary[j])
	PTArray.append(plaintextBinary[j+1])
	print("Result 0: "), result[0]
	print("Result 1: "), result[1]
	xor1 = int(result[0], 2) ^ int(PTArray[0], 2)
	xor2 = int(result[1], 2) ^ int(PTArray[1], 2)
	X1= '{0:b}'.format(xor1)
	X2= '{0:b}'.format(xor2)
	XORArray = []
	XORArray.append(int(X1 , 2))
	XORArray.append(int(X2 , 2))
	#print("XOR Array: "), XORArray
	result = encipher(XORArray, k)
	conn.send(pickle.dumps(result))
	
	#print ("Encryption result "), q
	#print (result)
	#print ("")
	q = q+1

EncryptedK0 = pow(k[0], e, n)
EncryptedK1 = pow(k[1], e, n)
EncryptedK2 = pow(k[2], e, n)
EncryptedK3 = pow(k[3], e, n)

EncryptedK = []

EncryptedK.append(EncryptedK0)
EncryptedK.append(EncryptedK1)
EncryptedK.append(EncryptedK2)
EncryptedK.append(EncryptedK3)

print("EncryptedK: "), EncryptedK
print("")

EncrK= pickle.dumps(EncryptedK)
conn.send(EncrK)

import pickle

#send IV to server
conn.send(pickle.dumps(NewIVArray))

FinalDigest = conn.recv(BUFFER_SIZE).decode()
print("Finale Digest: "), FinalDigest
#print("Length of XOR oUTPUT: "), len(xorOutput)
#Cast the plaintext into an unsigned integer. it sees the plaintext as chunks of 4 bytes(32 bits) each. 
#So you encrypt two 32 bits of the plaintext 
conn.close()



