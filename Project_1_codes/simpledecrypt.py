#decrypting with a shift cipher by exhaustion -Written by by Nick
def shift_decrypt(msg):
    '''
    Prints out all 25 iterations of our message using a shift cipher
    (I feel comfortable brute forcing this since 25 iterations is not the most
     resource intensive).

    PARAMETERS
    ----------
    msg: Message to decrypt

    RETURNS
    -------
    Does not return anything yet. When called this method

    TODO:
    -----
    Possibly make this function return a .txt file with each decrypted message

    '''

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # String of letters.
    ##########################################################################
    # I could use a list or array above to use some less obscure methods but #
    # I didn't want to type each letter                                      #
    # -Nick                                                                  #
    ##########################################################################


    for key in range(len(alpha)): # Here we start checking each key
        out = '' # Output initialized each time
        for i in msg: # Run through each letter in msg
            if i in alpha: # An error catcher in case a character isn't in msg
                decrypt = alpha.find(i) - key # Space bewteen the key w're testing
                if decrypt < 0: # Check if we get a negative value in our key and do a wrap around
                    decrypt = decrypt + 26 # We are using 26 letters
                out = out + alpha[decrypt] # Adds onto output
            else:
                out = out + i #same as above

        print(f"KEY {key} ({alpha[key]}): {out} ")
    return None

#decrypting with a affine cipher -Written by Carson
def affine_decrypt_key(encrypted_message, key):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
