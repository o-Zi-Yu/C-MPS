import sys
from functools import partial


if (len(sys.argv) != 3):
    print("args: .wav to .txt")
    exit(0)


wavfile = sys.argv[1]
txtfile = sys.argv[2]

fileread = open(wavfile, 'rb')
filewrite = open(txtfile, 'w')

n = 0
a = 0
b = 0

with open(wavfile, 'rb') as openfileobject:
    for data in iter(partial(openfileobject.read, 2), b''):
        dataw = hex(int.from_bytes(data, byteorder='big', signed=False))
        a += 1
        if a >= 70000:
            n += 1
            if n == 8:
                filewrite.write("\n")
                n = 0
            if dataw[:2]+dataw[4:] == "0x":
                filewrite.write("0x0"+", ")
            else:
                filewrite.write(dataw[:2]+dataw[4:]+", ")
            b += 1
            if b == 25000:
                break
    
print(a)
print(b)


fileread.close()
filewrite.close()