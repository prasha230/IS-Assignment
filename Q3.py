'''
Himanshu Sharma (25)
Prashant Rai (37)

Program 3
'''
import copy
def frequency_attack(S, N):
  # Stores first 10 possible deciphered plaintext
  plaintext = [None] * 10
  # Store the frequency of each letter in cipher text
  freq = [0] * 26
  # Stores the frequency of each letter in cipher text in descending order
  freqSorted = [None] * 26
  # Store which alphabet is used already
  used = [0] * 26
  # Traverse the string S
  for i in range(N):
      if S[i] != ' ':
          freq[ord(S[i]) - 65] += 1
  # Copy the frequency array        
  freqSorted=copy.deepcopy(freq)
  # Sort the array in descending order
  freqSorted.sort(reverse = True)
  # T Stores the string formed from concatanating the english letter in the decreasing frequency in the
  # english language    
  T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
  # Itearate over the range [0, 10]
  for i in range(10):
      ch = -1
      # Iterate over the range [0, 26]
      for j in range(26):
          if freqSorted[i] == freq[j] and used[j] == 0:
              used[j] = 1
              ch = j
              break
      if ch == -1:
          break
      # Store the numerical equivalent of letter
      # at ith index of array letter_frequency
      x = ord(T[i]) - 65
      # Calculate the probable shift used
      # in monoalphabetic cipher
      x = x - ch
      # Temporary string to generate one
      # plaintext at a time
      curr = ""
      # Generate the probable ith plaintext
      # string using the shift calculated above
      for k in range(N):
          # Insert whitespaces as it is
          if S[k] == ' ':
              curr += " "
              continue
          # Shift the kth letter of the
          # cipher by x
          y = ord(S[k]) - 65
          y += x
          if y < 0:
              y += 26
          if y > 25:
              y -= 26
          # Add the kth calculated/shifted
          # letter to temporary string    
          curr += chr(y + 65)
      plaintext[i] = curr
  return plaintext
def main():
    encrypted_word = input("\nEnter the encrypted message: ")
    print("\nFirst 10 possible plain texts are : ")
    text_list=frequency_attack(encrypted_word,len(encrypted_word))
    print(*text_list,sep='\n')
if __name__ == '__main__':
    main()