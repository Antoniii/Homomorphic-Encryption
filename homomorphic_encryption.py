# pip install phe
import phe

public_key, private_key = phe.generate_paillier_keypair(n_length=1024)

x = public_key.encrypt(4)

y = public_key.encrypt(2)

z = x + y

z_ = private_key.decrypt(z)
print("The answer: " + str(z_))
#print(z)