from Crypto.PublicKey import RSA

key = RSA.generate(3072)
sectret_code = "Unguessable"
encrypted_key = key.export_key(
    passphrase=sectret_code,
    pkcs=8,
    protection='scryptAndAES128-CBC',
    prot_params={'iteration_count': 131072}
)

with open('rsa_key.bin', 'wb') as f:
    f.write(encrypted_key)

print(key.publickey().export_key())