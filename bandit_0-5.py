from pwn import *

session = ssh('bandit0', 'bandit.labs.overthewire.org',2220, password='bandit0')
io = session.process('sh')
io.sendline('cat readme')
password1 = io.recvline().strip(b'$ \n')
print(password1)

session = ssh('bandit1', 'bandit.labs.overthewire.org', 2220, password = password1)
io = session.process('sh')
io.sendline('cat ./-')
password2 = io.recvline().strip(b'$ \n')
print(password2)

session = ssh('bandit2', 'bandit.labs.overthewire.org', 2220, password = password2)
io = session.process('sh')
io.sendline('cat \'spaces in this filename\'')
password3 = io.recvline().strip(b'$ \n')
print(password3)

session = ssh('bandit3', 'bandit.labs.overthewire.org', 2220, password3)
io = session.process('sh')
io.sendline('cd inhere')
io.sendline('cat .hidden')
password4 = io.recvline().strip(b'$ \n')
print(password4)

session = ssh('bandit4', 'bandit.labs.overthewire.org', 2220, password4)
io = session.process('sh')
io.sendline('cd inhere')
io.sendline('cat ./-file07')
password5 = io.recvline().strip(b'$ \n')
print(password5)

session = ssh('bandit5', 'bandit.labs.overthewire.org', 2220, password = password5)
io = session.process('sh')
io.interactive()

