import re

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()

    print('\n'.join(re.findall(r'\[\[Category:(.*?)(?:\|.*)?\]\]', text)))