import re
from knock_25 import extract_template_dic
from knock_26 import remove_stress
from knock_27 import remove_in_link

def remove_html(text):
    return re.sub("<.*?>", "", text)

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()

    template = extract_template_dic(text)

    for k in template.keys():
        template[k] = remove_stress(template[k])
        template[k] = remove_in_link(template[k])
        template[k] = remove_html(template[k])

    for k, v in template.items():
        print(k + ":" + v)