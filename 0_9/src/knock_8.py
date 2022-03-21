def cipher(text):
     res = [chr(219 - ord(c)) if "a" <= c <= "z" else c for c in text]
     return "".join(res)

if __name__ == "__main__":
    print(cipher("I can Speak in English"))
    print(cipher(cipher("I can Speak in English")))