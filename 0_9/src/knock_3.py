import re
def char_num(text):
    text = [re.sub(r'[,\.]', '', word) for word in text.split()]
    return [len(word) for word in text]

if __name__ == '__main__':
    text = 'Now I need a drink, alcoholic of course, \
    after the heavy lectures involving quantum mechanics.'
    print(char_num(text))