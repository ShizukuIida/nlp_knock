import re
def n_gram(n, text, fmt):
    if fmt == "char":
        words = [list(t) for t in re.sub(r"[,\.]", "", text).split()]
    else:
        words = [[t for t in re.sub(r"[,\.]", "", text).split()]]

    return [w[i:i+n] for w in words for i in range(len(w)-n+1)]

if __name__ == "__main__":
    text = "I am an NLPer"
    word_bi_gram = n_gram(2, text, "word")
    chars_bi_gram = n_gram(2, text, "char")

    print(word_bi_gram)
    print(chars_bi_gram)
