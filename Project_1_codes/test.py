import simpledecrypt as sd

#Test case for 6
msg1 = 'DBMXLKBLXABZAXLMTZTBGLMMAXPBGWGHMPBMABM - PBGLMHGVANKVABEE'
#sd.shift_decrypt(msg1)
#Test case for 5
msg2 = "AZEPCBBGYYCGXCPXXWPEIWREGYYCGXFZCPXWPE"
#sd.decrypt_affine_key(msg2, [7,2])
#Test cases for 7
msg3 = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'

msg4 = "GO"
sd.decrypt_affine_no_key(msg4, 26)
sd.decrypt_affine_key(msg4, [5,12])
#sd.decrypt_affine_key(msg3, [23,11])
