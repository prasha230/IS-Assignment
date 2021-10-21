'''
Himanshu Sharma (25)
Prashant Rai (37)

Program 5
'''
keyMatrix = [[0] * 2 for i in range(2)]
inverse_keyMatrix=[[0] * 2 for i in range(2)]
def getKeyMatrix(key):
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix
def get_inverse_keyMatrix():
    global inverse_keyMatrix
    det = (keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]) % 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i
            break
    inverse_keyMatrix = [[keyMatrix[1][1] * det % 26, -1 * keyMatrix[0][1] * det % 26],
                          [-1 * keyMatrix[1][0] * det % 26, keyMatrix[0][0] * det % 26]]
def encrypt(messageVector,length):
    cipherMatrix = [(keyMatrix[0][0]*messageVector[0]+keyMatrix[0][1]*messageVector[1])%26,(keyMatrix[1][0]*messageVector[0]+keyMatrix[1][1]*messageVector[1])%26]
    CipherText = []
    for i in range(2):
        CipherText.append(chr(cipherMatrix[i] + 65))
    if length==2:
      return "".join(CipherText)
    else:
      return CipherText[0]
def decrypt(encrypted_matrix,length):
    get_inverse_keyMatrix()
    decryptedMatrix = [(inverse_keyMatrix[0][0]*encrypted_matrix[0]+inverse_keyMatrix[0][1]*encrypted_matrix[1])%26,(inverse_keyMatrix[1][0]*encrypted_matrix[0]+inverse_keyMatrix[1][1]*encrypted_matrix[1])%26]
    decipherText = []
    for i in range(2):
        decipherText.append(chr(decryptedMatrix[i] + 65))
    if length==2:
      return "".join(decipherText)
    else:
      return "".join(decipherText[:1])
def HillCipher(message, key,choice):
    getKeyMatrix(key)
    rslt=""
    if choice==1:
        print('\n\tEncryted text : ',end='')
        while message!='':
            temp=message[:2]
            message=message[2:]
            messageVector = [0 for i in range(2)]
            if len(temp)==2:
              messageVector[0]=ord(temp[0])%65
              messageVector[1]=ord(temp[1])%65
              rslt+=encrypt(messageVector,2)
            else:
              messageVector[0]=ord(temp[0])%65
              messageVector[1]=(ord(temp[0])+1)%65
              rslt+=encrypt(messageVector,1)
        return rslt
    elif choice==2:
        print('\n\tDecrypted text : ',end='')
        while message!='':
            temp=message[:2]
            message=message[2:]
            messageVector = [0 for i in range(2)]
            if len(temp)==2:
              messageVector[0]=ord(temp[0])%65
              messageVector[1]=ord(temp[1])%65
              rslt+=decrypt(messageVector,2)
            else:
              messageVector[0]=ord(temp[0])%65
              messageVector[1]=(ord(temp[0])+1)%65
              rslt+=decrypt(messageVector,1)
        return rslt
    
def main():
    while True:
        print('\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : ',end='')
        choice=int(input())
        if(choice!=3):
            text=[x for x in input('Enter String : ').split()]
            key = "HILL"
            for i in text:
                rslt=HillCipher(i,key,choice)
                print(rslt)
        else:
            break
if __name__ == "__main__":
    main()
