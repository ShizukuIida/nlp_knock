import re

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()
        pattern = r"\[\[ファイル:(.+?)\|"
        res = re.findall(pattern, text)
        print("\n".join(res))