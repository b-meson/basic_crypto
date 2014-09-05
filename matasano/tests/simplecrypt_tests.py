#!/usr/bin/python

from nose.tools import *
import simplecrypt

def test_matasano1():
    hexstring = \
'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    
    answer = simplecrypt.hex_to_base64(hexstring)
    assert answer == \
'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def test_matasano2():
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    answer = simplecrypt.fixed_xor(input1, input2)
    assert answer == '746865206b696420646f6e277420706c6179'

def test_matasano3():
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    key, msg = simplecrypt.break_onechar_xor(cipher) 
    assert key == 'x'

def setup():
    pass

def teardown():
    pass

def test_basic():
    pass
