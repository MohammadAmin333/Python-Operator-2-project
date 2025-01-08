def is_alphabet(character):  
    if len(character) == 1 and character.isalpha():  
        return True  
    return False  

# Get user input  
char = input("Enter a character: ")  

# Check and display result  
if is_alphabet(char):  
    print(f"{char} is an alphabet.")  
else:  
    print(f"{char} is not an alphabet.")  