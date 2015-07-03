__author__ = 'dorcas'

def binary_rep(i):

     m = bin(i)
     n = m[2:]
     return n

def reverse_binary(n):
     """Take binary number y and reverse characters"""
     m = n[::-1]
     return m

def reverse_decimal(i):
     """Take decimal number i and reverse characters"""
     n = str(i)
     d = n[::-1]
     return d