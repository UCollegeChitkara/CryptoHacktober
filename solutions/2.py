import binascii
from hextobase64 import convertHex

str1 = b"1c0111001f010100061a024b53535009181c"
str2 = b"686974207468652062756c6c277320657965"
zipp = zip(convertHex(user1),convertHex(user2))
theList = ((chr((a^b)) for a,b in zipp))
theString = ("".join(theList))
finalBytes = theString.encode()
finalHex = binascii.b2a_hex(finalBytes)
print (finalHex)
