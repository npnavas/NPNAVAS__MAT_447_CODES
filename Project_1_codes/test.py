import simpledecrypt as sd

#Test case for 6
msg1 = 'PBGLMHGVANKVABEE'
sd.shift_decrypt(msg1)
#Test case for 5
msg2 = "AZEPCBBGYYCGXCPXXWPEIWREGYYCGXFZCPXWPE"
sd.decrypt_affine_key(msg2, [7,2])
#Test cases for 7
msg3 = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'
sd.decrypt_affine_no_key(msg3, 3)
sd.decrypt_affine_key(msg3, [3,8])
sd.decrypt_affine_key(msg3, [23,11])
