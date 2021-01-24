"""
Polymorphism means multiple forms which enables using a single interface
with input of different datatype, different class or may be for different number of inputs.

Program to find histogram to count the number of times each letter appear in a words and in a sentence
"""


def histogram(t):
    d = dict()
    sen = dict()
    result = dict()

    for word in t.split():
        tmp = dict()
        for letter in word:
            if letter not in tmp:
                tmp[letter] = 1
            else:
                tmp[letter] += 1
        d[word] = tmp

    for k, v in d.items():
        for x in v:
            if x not in sen:
                sen[x] = d[k][x]
            else:
                sen[x] += 1

    if len(t.split()) != 1:
        result[t] = sen
        return result, d
    else:
        return d


print(histogram("hello to everyone"))
print(histogram("gaurav"))
