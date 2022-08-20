alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#decrypting with a affine cipher
def decrypt(encrypted_message, key):

    print('ENCRYPTED MESSAGE: ' + encrypted_message)

    #blank output message
    decrypted_message = ''
    
    for encrypted_letter in encrypted_message:

        #get the numerical value of encrypted letter
        index = alpha.find(encrypted_letter)

        #blank candidates array
        candidates = []

        #fill up candidates for reverse modulo operation
        for i in range(0,key[0]):
            candidates.append(index + i*26)
        
        #subtract key[1] (as per the affine key)
        candidates = [x - key[1] for x in candidates]

        #loop through our candidates
        for candidate in candidates:

            #test if they are a multiple of key[0] (as they were generated using key[0] * an integer
            #there should only be one
            if(candidate % key[0] == 0):

                #append decrypted letter to decypted message
                decrypted_message = decrypted_message + alpha[int(candidate / key[0])]

    print('DECRYPTED MESSAGE: ' + decrypted_message)
        


message = 'AZEPCBBGYYCGXCPXXWPEIWREGYYCGXFZCPXWPE'
key = [7,2]

decrypt(message,key)
