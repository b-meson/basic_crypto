#!/usr/bin/python

"""
Solutions to Matasano's first set of cryptography challenges. 
As well as some bonus bits that might be useful for other things.
"""

import binascii
import base64
import numpy as np
import collections
import string
import array
from string import ascii_lowercase
import pdb

def hex_to_ascii(hexstring):
    in_ascii = binascii.unhexlify(hexstring) 
    return in_ascii

def hex_to_base64(hexstring): 
    in_base64 = base64.b64encode(hex_to_ascii(hexstring))
    return in_base64

def base64_to_ascii(b64string):
    in_ascii = base64.b64decode(b64_input)
    return in_ascii

def base64_to_hex(b64string):
    in_hex = binascii.hexlify(base64_to_ascii(b64string))
    return in_hex

def fixed_xor(string1, string2):
    xor_decimal = int(string1, 16) ^ int(string2, 16)
    xor_answer = hex(xor_decimal)
    return xor_answer.rstrip('L').lstrip('0x')

def onechar_xor(singlechar, text):
    repeat_times = len(text)/2
    test_key = singlechar * repeat_times
    xor_answer = fixed_xor( text,test_key.encode('hex')).zfill(len(text))
    xor_ascii = xor_answer.decode('hex') 

    # Fix \x00 and \x07
    xor_ascii = xor_ascii.replace('\x00',' ')
    xor_ascii = xor_ascii.replace('\x07','\'')

    return xor_ascii

def break_onechar_xor(ciphertext):
    keys = string.lowercase+string.uppercase

    # Baseline char frequencies
    english_weights = 0.065 # From Katz, Lindell crypto text
    test_weights = np.zeros(len(keys)) 
    for x in range(0, len(keys)):
        # xor this key with the ciphertext
        xor_ascii = onechar_xor(keys[x], ciphertext)

        # score the result based on character frequencies
        test = collections.defaultdict(int)
        for y in string.lower(xor_ascii):
            test[y] += 1

        normalize = float(len(xor_ascii))
        intermed_weight = array.array('f')
        for z in ascii_lowercase:
            intermed_weight.append(test[z]/normalize)
        weights = np.array(intermed_weight)
        weight_score = sum(weights ** 2)
        test_weights[x] = weight_score
        
    # Determine which is the closest to English character frequencies
    key_index = np.abs(test_weights - english_weights).argmin(axis=0)
    key_answer = keys[key_index]
    answer_ascii = onechar_xor(key_answer, ciphertext)

    return key_answer, answer_ascii

def detect_onechar_xor(ciphertexts):
    # Add 
    return ciphertext
