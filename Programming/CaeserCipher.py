alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
print ("Encryption tool")
choice = input ("Encrypt, Decrypt or Quit: ")
if choice.lower() == "encrypt":
    plaintext = input ('Enter Message: ')
    cipher = ''
    key = input ('Enter Key: ')
    key = int (key)
    for c in plaintext:
        if c in alphabet:
            cipher += alphabet [(alphabet.index(c)-key)%(len(alphabet))]
    print ('Your encrypted message is: ' + cipher)
    
    choice = input ("Encrypt, Decrypt or Quit: ")
    if choice.lower() == "encrypt":
        plaintext = input ('Enter Message: ')
        cipher = ''
        key = input ('Enter Same Key: ')
        key = int (key)
        for c in plaintext:
            if c in alphabet:
                cipher += alphabet [(alphabet.index(c)-key)%(len(alphabet))]
                print ('Your encrypted message is: ' + cipher)
        
    elif choice.lower() == "decrypt":
        key = input ('Enter Same Key: ')
        key = int (key)     
        plaintext = input ('Enter Encrypted Message: ')
        cipher = ''   
        for c in plaintext:
            if c in alphabet:
                cipher += alphabet [(alphabet.index(c)+key)%(len(alphabet))]
                print ('Your decrypted message is: '  + cipher)   
                
    elif choice.lower() == "quit":
        print ("Game Over")
                
elif choice.lower() == "decrypt":
    key = input ('Enter Key: ')
    key = int (key)     
    plaintext = input ('Enter Encrypted Message: ')
    cipher = ''   
    for c in plaintext:
        if c in alphabet:
            cipher += alphabet [(alphabet.index(c)+key)%(len(alphabet))]

    print ('Your decrypted message is: ' + cipher)
    
elif choice.lower() == "quit":
    print ("Game Over")
