import re
from knock_25 import extract_template_dic

def remove_stress(text):
    pattern = r"\'{2,5}"
    return re.sub(pattern, '', text)

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()

    template = extract_template_dic(text)

    for k in template.keys():
        template[k] = remove_stress(template[k])

    for k, v in template.items():
        print(k + ":" + v)


