#!/usr/bin/env python3
# -*_ coding: UTF-8 -*_

hexStr = ''
hexChars = ['0','1','2','3','4','5','6','7','8','9',
'A','B','C','D','E','F'];

dec = int(input('Enter a decimal number: '))
decSave = dec 
while dec > 0:
    hexDigit = dec % 16;
    hexStr = hexChars[hexDigit] + hexStr;
    dec = dec // 16;

print('The hex for decimal {} is: {}'.format(decSave, hexStr))

print('The hex for decimal {} using build-in function is: {} '.format(decSave,hex(decSave)))

'''
>>> format(1234, 'x')
'4d2'
>>> format(1234,'X')
'4D2'
>>> fromat(1234, 'o')
'2322'
>>> format(1234, 'b')
'10011010010'
>>> format(0x4d2, 'b')
'10011010010'
>>> hex(1234)
'0x4d2'
>>> oct(1234)
'0o2322'
>>> bin(1234)
'0b10011010010'

'''

"""
>>> str = 'hello'
>>> ''.join(format(ord(ch),'x')for ch in str)
'68 65 6c 6c 6f'
"""