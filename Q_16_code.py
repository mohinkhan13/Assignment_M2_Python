'''
Write a Python program to count the occurrences of each word in a
given sentence

'''
st = input("Please enter a sentence: ")

words = st.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
        
for word, frequency in word_freq.items():
    print(f"'{word}' appears {frequency} times")
