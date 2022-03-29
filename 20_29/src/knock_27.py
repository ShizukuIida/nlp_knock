import re
from knock_25 import extract_template_dic
from knock_26 import remove_stress

def remove_in_link(text):
    pattern = "(.*?)\[\[(.*?)\]\](.*)"
    word = re.search(pattern, text)
    if word is not None:
        while True:
            if word.groups()[1][:4] not in ['ファイル', 'http', 'Cate']:
                link_word = word.groups()[1].split('|')[-1]
                text = word.groups()[0] + link_word + word.groups()[2]
            else:
                break
            word = re.search(pattern, text)
            if word is None:
                break

    return text

if __name__ == "__main__":
    with open("../data/wiki_england.txt", "r") as f:
        text = f.read()

    template = extract_template_dic(text)

    for k in template.keys():
        template[k] = remove_stress(template[k])
        template[k] = remove_in_link(template[k])

    for k, v in template.items():
        print(k + ":" + v)