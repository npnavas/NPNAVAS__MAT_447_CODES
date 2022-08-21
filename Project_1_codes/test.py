import simpledecrypt as sd

msg1 = 'PBGLMHGVANKVABEE'
sd.shift_decrypt(msg1)

msg2 = "AZEPCBBGYYCGXCPXXWPEIWREGYYCGXFZCPXWPE"
sd.decrypt_affine_key(msg2, [7,2])

msg3 = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'
sd.decrypt_affine_no_key(msg3, 3)
