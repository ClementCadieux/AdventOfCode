import hashlib
import sys
from util import readFile

if __name__ == "__main__":
    filePath = "2015\\Day4\\test.txt" if len(sys.argv) < 2 else sys.argv[1]

    line = readFile(filePath)

    key = 1

    while True:
        secretKey = line + str(key)

        encodedKey = secretKey.encode("utf-8")

        md5_hash = hashlib.md5()

        md5_hash.update(encodedKey)

        digest = md5_hash.hexdigest()

        valid = True

        for i in range(5):
            if digest[i] != "0":
                valid = False
        
        if valid:
            break

        key += 1
    
    print(key)