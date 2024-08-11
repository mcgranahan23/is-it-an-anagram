import unicodedata
def is_anagram(left, right):
    
    left1 = unicodedata.normalize('NFD', left)
    right1 = unicodedata.normalize('NFD', right)
    
    for letter in left1:
        
        if unicodedata.combining(letter) != 0:
            left1 = left1.replace(letter, '')
            
    for letter in right1:
           
        if unicodedata.combining(letter) != 0:
            right1 = right1.replace(letter, '')
            
    left1 = left1.lower()
    right1 = right1.lower()
    left1 = ''.join(letter for letter in left1 if letter.isalnum())
    right1 = ''.join(letter for letter in right1 if letter.isalnum())
    
    if (sorted(left1) == sorted(right1)):
        return True
