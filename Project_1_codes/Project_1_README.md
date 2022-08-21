To run shift decrypt make a new .py file and do
```
import simpledecrypt as sd
```
And example of how to use this package would be as follows:
```
import simpledecrypt as sd

msg1 = 'PBGLMHGVANKVABEE'
sd.shift_decrypt(msg1)

msg2 = "AZEPCBBGYYCGXCPXXWPEIWREGYYCGXFZCPXWPE"
sd.decrypt_affine_key(msg2, [7,2])

msg3 = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'
sd.decrypt_affine_no_key(msg3, 3)

```
The file letter_freq.py is a way you can find the amount of times a letter pops up in a message. This is used for question 7.
