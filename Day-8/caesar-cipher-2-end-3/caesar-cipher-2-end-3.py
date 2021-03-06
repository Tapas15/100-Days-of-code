alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      position = alphabet.index(letter)
      new_position = position + shift_amount
      alphabet_length = len(alphabet) - 1
      if new_position > alphabet_length:
        new_position -= alphabet_length
      elif new_position < 0:
        new_position += alphabet_length
      new_char = alphabet[new_position]
      end_text += new_char
    
  print(f"Here's the {direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Hint: Think about how you can use the modulus (%).


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)