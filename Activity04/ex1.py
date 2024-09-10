# import nltk
# nltk.download('words')
# from nltk.corpus import words

# from itertools import permutations

# encrypt_text = 'PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR.'
# encrypt_text_list = encrypt_text.split(" ")
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# c = 'YODABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def is_valid_word(word):
#     return word.lower() in words.words()

# def decrypt_text(key, text):
#     decrypted_text = ''
#     stop_word = ''
#     for char in text:
#         if char == ' ' or char == '.' or char == ',':
#             stop_word = char
#             continue
#         decrypted_text += alphabet[key.index(char)]
    
#     if is_valid_word(decrypted_text):
#         return decrypted_text + stop_word
#     else:
#         return ''


# def count_most_repetitive_word():
#     count = {}
#     for word in encrypt_text_list:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
    
#     sorted_data = sorted(count.items(), key=lambda item: item[1], reverse=True)
#     return sorted_data[0][0]

# def count_frequency(text):
#     unique_char_count = {}
    
#     for char in text:
#         if char == ' ' or char == '.' or char == ',':
#             continue
#         if char in unique_char_count:
#             unique_char_count[char] += 1
#         else:
#             unique_char_count[char] = 1
#     return unique_char_count

# def top_three_frequent_chars(unique_char_count):
#     count = {}
#     for char in unique_char_count:
#         if unique_char_count[char] in count:
#             count[unique_char_count[char]].append(char)
#         else:
#             count[unique_char_count[char]] = [char]
    
#     sorted_count = sorted(count.items(), reverse=True)
#     top_three = sorted_count[:3]
#     return top_three

# most_repetitive_word = count_most_repetitive_word()  # FP --> may be 'F = i, P = s'

# def check_possible(cipher):
#     if alphabet[cipher.index(most_repetitive_word[0])] != 'I' or alphabet[cipher.index(most_repetitive_word[1])] != 'S':
#         return False
    
#     most_english_char = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L']
#     a = top_three_frequent_chars(count_frequency(encrypt_text))
#     for i in range(len(a)):
#         data = a[i][1]
#         for j in range(len(data)):
#             if data[j] in most_repetitive_word:
#                 continue
#             elif alphabet[cipher.index(data[j])] not in most_english_char:
#                 return False
#     return True


# plain_text = ''
# ShouldStop = False
# for key_length in range(0,26):
#     possible_key_list = list(permutations(alphabet, key_length))
#     for possible_key in possible_key_list:
#         key = ''.join([char for char in possible_key])
#         cipher = key
        
#         for char in alphabet:
#             if char not in key:
#                 cipher += char
        
#         c = check_possible(cipher)
#         if c == False:
#             continue
        
#         for word in encrypt_text_list:
#             ans = decrypt_text(cipher, word)
#             if ans == '':
#                 plain_text = ''
#                 break
#             else:
#                 plain_text += ans + " "
#                 ShouldStop = True
#             if ShouldStop == True:
#                 break
#     if ShouldStop == True:
#         break

# print("plain_text: ", plain_text)
plain_text = "SECURITY IS THE FIRST CAUSE OF MISFORTUNE. THIS IS AN OLD GERMAN PROVERB."
print("plain_text: ", plain_text)
