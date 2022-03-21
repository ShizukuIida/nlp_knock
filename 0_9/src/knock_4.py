import re
def create_element_map(text, pos_list):
    text = [re.sub(r'[.\.]', '', word) for word in text.split()]
    dic = {}
    for i in range(len(text)):
        if i + 1 in pos_list:
            dic[text[i][:1]] = i + 1
        else:
            dic[text[i][:2]] = i + 1

    return dic

if __name__ == "__main__":
    text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.\
     New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    
    pos_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    print(create_element_map(text, pos_list))