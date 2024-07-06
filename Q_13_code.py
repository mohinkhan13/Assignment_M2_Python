'''
 Write a Python program to count the number of characters (character 
frequency) in a string

'''

st = input("please Enter String : ")

dubli = {}

for ch in st:
    if ch == ' ':
        continue
    
    if ch in dubli:
        dubli[ch] +=1
    else:
        dubli[ch] =1

for ch,fq in dubli.items():
    print(ch ," : ",fq)