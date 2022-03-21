from knock_5 import n_gram

if __name__ == "__main__" :
    t1 = "paraparaparadise"
    t2 = "paragragh"
    bi1 = {"".join(t) for t in n_gram(2, t1, "char")}
    bi2 = {"".join(t) for t in n_gram(2, t2, "char")}

    print("和集合:", bi1 | bi2)
    print("積集合:", bi1 & bi2)
    print("差集合:", bi1 - bi2)
    print("'se' in X:", 'se' in bi1)
    print("'se' in Y:", 'se' in bi2)
