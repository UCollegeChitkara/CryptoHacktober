import binascii
from hextobase64 import convertHex

# predefined strings for testing the function
str1 = b"1c0111001f010100061a024b53535009181c"
str2 = b"686974207468652062756c6c277320657965"

# function to XOR two strings
def xorStr(user1, user2):
    if(len(user1)==len(user2)):
        # Make an iterator that aggregates elements from each of the raw strings.
        zipp = zip(convertHex(user1),convertHex(user2))
        # XOR of elements
        theList = ((chr((a^b)) for a,b in zipp))
        # making of the string
        theString = ("".join(theList))
        # turning string to bytes
        finalBytes = theString.encode()
        # turning bytes to hex
        finalHex = binascii.b2a_hex(finalBytes)
        #skadooooooosh
        print (finalHex)

    else:
        print("Enter two strings with same length")

if __name__ == "__main__":
    xorStr(str1, str2)
