'''
Himanshu Sharma (25)
Prashant Rai (37)

Program 1
'''

def encrypt(text,shift):      #performs encryption using caeser cipher
  encrypted_text=""
  for i in text:
    if (i.isupper()):
      encrypted_text += chr((ord(i) + shift-65) % 26 + 65)
    else:
      encrypted_text += chr((ord(i) + shift - 97) % 26 + 97)
  return encrypted_text
def decrypt(text,shift):    #decrypts encrypted text
  decrypted_text=""
  for i in text:
    if (i.isupper()):
      decrypted_text += chr((ord(i) - shift-65) % 26 + 65)
    else:
      decrypted_text += chr((ord(i) - shift - 97) % 26 + 97)
  return decrypted_text
def main():               #main driver function
  while True:
    choice=int(input("\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : "))
    if choice==1:
      text=input("Enter the Plain Text : ")
      shift=int(input('Enter the Shift Value : '))
      print("\n\nEncrypted Text - ",encrypt(text,shift))
    elif choice==2:
      text=input("Enter the encrypted Text : ")
      shift=int(input('Enter the Shift Value : '))
      print("\n\nDecrypted Text - ",decrypt(text,shift))
    else:
      break
main()
