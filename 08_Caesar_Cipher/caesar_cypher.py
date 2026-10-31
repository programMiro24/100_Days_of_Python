import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    result = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            result += letter
            continue
        number = (alphabet.index(letter) + shift_amount)%len(alphabet)
        result += alphabet[number]
    print(f"Here is the {encode_or_decode}d message: {result}")

running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid input! Try again.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        print("Goodbye!")
        running = False