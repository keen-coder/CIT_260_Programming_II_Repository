'''
Programming Assignment 3

<Your First and last name>
<Your Class and section number>
'''

#This is the encrypted string that you must convert back into a meaningful sentence.
ENCRYPTED = '342914-467980197300000-38412000-3885-13402296-67094560500-41358661344-62141664-33928155600-1102962420-685898930883600-9079200-92400-3767400-2905980-31082158140'

'''
==Counting Word Frequency==
'''
#1 - Open sample_text.txt and save its contents to a variable

#2 - Normalize words by making all capitals lowercase, eliminating punctuation, etc.

#3 - Convert the sample_text contents into a list of each word

#4 - Create a dictionary named 'counts' (or similar)

#5 - Count the frequency of each word. Each word is a key, its value is how often it occurs
#    Ex: {'apple': 5, 'orange': 2...}

'''
==Save counts to a File==
'''
#6 - Create and open a binary file named 'counts.dat'

#7 - Serialize (pickle) 'counts' dictionary and write to 'counts.dat'


'''
==Generate Key==
'''
#8 - Create a dictionary named 'decryption_key' (or similar)
    
#9 - Loop through each word in 'counts' dictionary
#  - Ignore all words that only have 1 occurance

#10 - Create encryption number of each word 
    #A - number starts at 1
    #B - Multiply number by how often it occurs
    #C - For each character in the word, multiply number by ord() of that character

#11 - Set the encryption number as a key with its word as the value
#   - Ex: {12385: 'hi', 521348: 'it'...}

'''
==Save decryption_key to a File==
'''
#12 - Serialize (pickle) 'decryption_key' dictionary and write to 'decryption_key.dat'

'''
==Decrypt==
'''
#13 - Use 'decryption_key' to translate each number in ENCRYPTED into a word
#   - Each dash should be a space

#14 - Print decrypted sentence




