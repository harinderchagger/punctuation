import string
punctuations = string.punctuation

def punct(n):
    file = open(n,"r")
    for line in file:
        line_strip = line.strip()
        line_split= line_strip.split()
        for word in line_split:
            for ch in punctuations:
                word=word.replace(ch,"")
            word = word.lower()
            print(word,end=" ")
        print()

punct("pbook.txt")