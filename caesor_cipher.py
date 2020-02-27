#maximun value for KEY should be less then 25
def encryption(plain_text,key):
    cipher_text = ''
    sentence = list(plain_text)
    join_sentence = ''
    
    for j in sentence:
    
        if j == ' ':
            join_sentence += '$' 
        else:
            join_sentence += j
    letters = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

    for i in join_sentence:
        if i == '$':
            cipher_text += '$'
        else:
            cipher_text = cipher_text + letters[letters.index(i) + key]
    
    print("your encrypted cipher text is:==" + " "  + cipher_text)

def decrytion(cipher_text,key):
    plain_text = ''
    sentence = list(cipher_text)
    join_sentence = ''
    for j in sentence:
        if j == '$':
            join_sentence += ' ' 
        else:
            join_sentence += j
    letters = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    
    for i in join_sentence:
        
        if i == ' ':
            plain_text += ' '
        else:
            plain_text += letters[letters.index(i) - key]
    
    print("your decrypted cipher text is:==" + " "  + plain_text)



plain_text = input("Enter your Plain text:=" + "  ")
key = int(input("enter your KEY:=" + "  "))
encryption(plain_text,key)
cipher_text = input("Enter your cipher text:=" + "  ")
key = int(input("enter your KEY:=" + "  "))
decrytion(cipher_text,key)
