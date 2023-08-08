import sys
# copy the ep7n string to a file and pass the filename as the first command line arg
ep7n = open(sys.argv[1], 'rb').read()
print ep7n[0:2]
a = int(ep7n[0:2],16)
b = a ^ ord('9')
print hex(b)
rwUg8U = "".join([chr(int(ep7n[i:i+2], 16)) for i in xrange(0, len(ep7n)-1, 2)])
iTtZC4r0PfQ="92MfVftkHPlUUB2Vm4mBfhBdH0TQ3NInxpID0B3E7PzPVyCTFjKvm1P76ecvMgHOcvHuSaj2VAf1WaXpC7dGSk"
yePFwrYn4TqS2=""
for i in range(len(rwUg8U)):
 curXor = ord(iTtZC4r0PfQ[ i % len(iTtZC4r0PfQ) ] )
 print hex(curXor)
 print hex(ord(rwUg8U[i]) ^ curXor)
 yePFwrYn4TqS2 += chr(ord(rwUg8U[i]) ^ curXor)
 print hex(ord(yePFwrYn4TqS2[i]))
fp_out = open(sys.argv[2], 'wb')
fp_out.write(yePFwrYn