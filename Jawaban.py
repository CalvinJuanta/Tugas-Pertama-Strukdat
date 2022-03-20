'''
Created on Mar 20, 2022

@author: Calvin
'''
def write_binary():
    binary = open("tugas pertama", "wb")
    binary.write(bytes(b'\ tugas pertama strukdat'))
    binary.close()
    
write_binary()