import mono_hack as mc

cipher = mc.random_monoalpha_cipher()
print(cipher)
encrypted = mc.encrypt_with_monoalpha('Hello all you hackers out there!', cipher)
decrypted = mc.decrypt_with_monoalpha('Acggk mgg wky ambfcoi kyu uacoc!', cipher)

print(encrypted)
print(decrypted)