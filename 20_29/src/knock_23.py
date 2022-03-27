import re

if __name__ == "__main__":
     with open("../data/wiki_england.txt", "r") as f:
        text = f.read()

     pattern = r"^(\={1,})\s*(.+?)\s*(\={1,}).*$"
     mach = re.findall(pattern, text, re.MULTILINE)
     res = [(section[1] + ':' + str(len(section[0])-1)) for section in re.findall(pattern, text, re.MULTILINE)]
     print('\n'.join(res))