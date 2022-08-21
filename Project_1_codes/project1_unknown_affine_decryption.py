
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#helper functions
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1



#pass me a message and a key
def decrypt_affine(encrypted_message,key):

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

    return decrypted_message



#pass me your decrypted message and the max multiplier you want to test
def decrypt(message, limit):

    #iterate up to our limit
    for i in range(0,limit):

        #we only check numbers relatively prime with 26, (those will be one-to-one)
        if(coprime(i,26)):
            print('FOR MULTIPLIER = ' + str(i))

            #for each multiplier, we check all shifts 0 through 25
            for j in range(0,26):
                print('Shift ' + str(j) + ': ' + decrypt_affine(message,[i,j]))
        


message = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'

decrypt(message,85)
print(message)

#look at 81x+8 !

