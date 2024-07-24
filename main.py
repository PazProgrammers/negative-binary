num = int(input())
bits = int(input())
binNum = str(bin(num)[2:])
opBinNum = ""
for i in range(bits - len(binNum)):
    binNum = "0" + binNum
for bit in binNum:
    if bit == "0":
        opBinNum += "1"
    else:
        opBinNum += "0"
negBinNum = ""
done = False
for bit in reversed(opBinNum):
    if done:
        negBinNum = bit + negBinNum
    elif bit == "1":
        negBinNum = "0" + negBinNum
    else:
        negBinNum = "1" + negBinNum
        done = True
print(negBinNum)