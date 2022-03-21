def mutually_joint(text1, text2):
    return ''.join([i + j for i, j in zip(text1, text2)])

if __name__ == "__main__":
    print(mutually_joint("パトカー", "タクシー"))