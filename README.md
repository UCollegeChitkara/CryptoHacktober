# CryptoHacktober
A repo with an introduction to cryptography, resources and info.

## Introduction to Cryptography :
Cryptography is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it.      

Cryptography includes techniques such as microdots, merging words with images, and other ways to hide information in storage or transit. Cryptography is most often associated with scrambling plaintext (ordinary text, sometimes referred to as cleartext) into ciphertext (a process called encryption), then back again (known as decryption). 

Modern cryptography concerns itself with the following four objectives:

* Confidentiality (the information cannot be understood by anyone for whom it was unintended)

* Integrity (the information cannot be altered in storage or transit between sender and intended receiver without the alteration being detected)

* Non-repudiation (the creator/sender of the information cannot deny at a later stage his or her intentions in the creation or transmission of the information)

* Authentication (the sender and receiver can confirm each other?s identity and the origin/destination of the information)

----
## Exclusive OR (XOR) :

Output of XOR is 1 when one input or the other (but not both) is 1:
```
0 ⊕ 0 = 0 
1 ⊕ 0 = 1
0 ⊕ 1 = 1 
1 ⊕ 1 = 0
```
There are a few useful arithmetic tricks we can derive from that.

1. You can apply XOR in any order: a ⊕ (b ⊕ c) = (a ⊕ b) ⊕ c

2. You can flip the operands around: a ⊕ b = b ⊕ a

3. Any bit XOR itself is 0: a ⊕ a = 0. If a is 0, then it’s 0 ⊕ 0 = 0.

4. Any bit XOR 0 is that bit again: a ⊕ 0 = a. If a is 0, then it’s 0 ⊕ 0 = 0.

These rules also imply a ⊕ b ⊕ a = b:
a ⊕ b ⊕ a = a ⊕ a ⊕ b (second rule)
= 0 ⊕ b (third rule)
= b (fourth rule)
