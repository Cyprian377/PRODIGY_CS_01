FIRST_CHAR_CODE=ord("A")
LAST_CHAR_CODE=ord("Z")
CHAR_RANGE=LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_encryption(message, shift):
        #result placeholder FIRST_CHAR_CODE=ord("A")
    result=""
    for char in message.upper():
        if char.isalpha():

            char_code=ord(char)
            new_char_code=char_code + shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            elif new_char_code < FIRST_CHAR_CODE:
                new_char_code +=CHAR_RANGE
            new_char=chr(new_char_code)
            result+= new_char
        else:
             result += char
    print(result)


def caesar_decryption(encrypted_message, shift):
     #result placeholder FIRST_CHAR_CODE=ord("A")
    result=""
    for char in encrypted_message.upper():
        if char.isalpha():

            char_code=ord(char)
            new_char_code=char_code - shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code += CHAR_RANGE
            elif new_char_code < FIRST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            new_char=chr(new_char_code)
            result += new_char
        else:
             result += char
        
    print(result)
def main():
        while True:
            print("Caesar Cipher Menu: ")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Quit")
            choice=input("chose options: ")

            if choice == "1":
                users_message = input("Enter the message to encrypt: ")
                shift_key = int(input("Enter the shift value: "))
                encrypted_message =caesar_encryption(users_message, shift_key)
                break
            elif choice == "2":
                encrypted_message = input("Enter the message to decrypt: ")
                shift = int(input("Enter the shift value: "))
                decrypted_message = caesar_decryption(encrypted_message, shift)
                break 
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




