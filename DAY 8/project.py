
 # Output: Hello World

print('''

____    _    _____ ____    _    ____    
 / ___|  / \  | ____/ ___|  / \  |  _ \   
| |     / _ \ |  _| \___ \ / _ \ | |_) |  
| |___ / ___ \| |___ ___) / ___ \|  _ <   
 \____/_/   \_\_____|____/_/   \_\_| \_\  
                                          
  ____ ___ ____  _   _ _____ ____  
 / ___|_ _|  _ \| | | | ____|  _ \ 
| |    | || |_) | |_| |  _| | |_) |
| |___ | ||  __/|  _  | |___|  _ < 
 \____|___|_|   |_| |_|_____|_| \_\

''') 
while True:
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    direction = input("Type 'encode' to encrypt type 'decode' to decryypt").lower()

    text = input("type your message:\n").lower()
    shift= int(input("Type the shift number"))

    def encrypt(original_text,shift_amout):
        encode =""
        for letter in original_text:
            shifted_letter = alphabet.index(letter)+shift_amout
            encode += alphabet[shifted_letter]
        print(encode)

    def decrypt(original_text,shift_amout):
        decode =""
        for letter in original_text:
            shifted_letter = alphabet.index(letter)-shift_amout
            decode += alphabet[shifted_letter]
        print(decode)


    if(direction== "encode"):
        encrypt(text,shift)
    elif(direction=="decode"):
        decrypt(text,shift)
    else:
        print("Enter the right choice")
        
