import ceaser_art
def ceasar(giventext,shift,dir):
    endtext=""
    for letter in giventext:
        if letter in alphabet:
            for position in range(len(alphabet)):
                if alphabet[position] == letter:
                    if dir=="decode":
                     endtext+=alphabet[position-shift]
                    elif dir=="encode":
                        if (len(alphabet)-1)-position>=shift:
                            endtext+=alphabet[position+shift]
                        else:
                            shiftfromstart=shift-((len(alphabet)-1)-position)
                            print(shiftfromstart)
                            endtext+=alphabet[shiftfromstart-1]
        else:
            endtext+=letter
    print(f"The {dir}d text is {endtext}")

continueencrypting="True"

print(ceaser_art.logo)
while continueencrypting:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Enter your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ceasar(text,shift,direction)
    continueencrypting=input("Do you want to continue? Y/N").lower()
    if continueencrypting =="y":
        continueencrypting=True
    else:
        continueencrypting=False
        print("goodbye")