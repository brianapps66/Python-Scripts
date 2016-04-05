import sys
import hashlib

secret_key = 'bgvyzdsv'

for i in range(0,sys.maxsize):
    combined = secret_key+str(i)
    m=hashlib.md5()
    m.update(combined.encode())
    md5_result = m.hexdigest()
    if md5_result[:6] == '000000':
        print(combined)
        print(md5_result)
        break
