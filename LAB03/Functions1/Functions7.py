def reverse_sentence(sentence):
    words = sentence.split()
    rwords = words[::-1]
    rsentence="  ".join(rwords)
    return rsentence
sentence = input()
print(reverse_sentence(sentence))
