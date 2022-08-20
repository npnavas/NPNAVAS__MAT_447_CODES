To run shift decrypt make a new .py file and do
```
import simpledecrypt as sd
```
To decrypt a shift cipher do the following:
```
msg = 'YOUR ENGLISH STRING HERE'
sd.shift_decrypt(msg)
```
For affine ciphers with a known key do the following:
```
msg = 'YOUR ENGLISH STRING HERE'
key = [a,b] #a,b are int for our key being in the form ax+b (mod 26)
sd.affine_decrypt_key(msg,key)
=======
import shift_decrypt as sd
msg = 'YOUR ENGLISH STRING HERE'
sd.decrypt(msg)
>>>>>>> cef15e3eb5363679e9451764cf6b84a6c1a34aa7
```
