import re

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()
        pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
        template = re.findall(pattern, text, re.MULTILINE + re.DOTALL)

        pattern = "^\|(.+?)\s+=\s*(.+?)(?:(?=\n\|)|(?=\n|$))"
        res = re.findall(pattern, template[0], re.MULTILINE + re.DOTALL)

        dic = {}
        for k, v in res:
            dic[k] = v
        print(dic)
