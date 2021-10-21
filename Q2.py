'''
Himanshu Sharma (25)
Prashant Rai (37)

Program 2
'''
def egcd(a, b):                 #calculating gcd
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y
def modinv(a, m):               #calculates and returns inverse
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m
def affine_encrypt(text, key):  #performs encryption
    rslt=""
    for i in text:
        if i!=' ' and i.isupper():
            rslt+=chr((key[0]*(ord(i)-65)+key[1])%26+65)
        elif i!=' ' and i.islower():
            rslt+=chr((key[0]*(ord(i)-97)+key[1])%26+97)
        else:
            rslt+=' '
    return rslt
def affine_decrypt(cipher, key):    #performs decryption
    rslt=""
    for i in cipher:
        if i!=' ' and i.isupper():
            rslt+=chr((modinv(key[0],26)*(ord(i)-65-key[1]))%26+65)
        elif i!=' ' and i.islower():
            rslt+=chr((modinv(key[0],26)*(ord(i)-97-key[1]))%26+97)
        else:
            rslt+=' '
    return rslt
def main():                         #main driver function
    while True:
        choice=int(input("\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : "))
        if choice==1:
            text=input("Enter the Plain Text : ")
            key = [int(x) for x in input('Enter Key(Space separated) : ').split()][:2]
            print("\n\nEncrypted Text - ",affine_encrypt(text,key))
        elif choice==2:
            text=input("Enter the encrypted Text : ")
            key = [int(x) for x in input('Enter Key(Space separated) : ').split()][:2]
            print("\n\nDecrypted Text - ",affine_decrypt(text,key))
        else:
            break
if __name__ == '__main__':
	main()
