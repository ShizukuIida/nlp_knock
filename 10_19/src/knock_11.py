#python knock_11.py ../data/popular-names.txt
#tr '\t' '' < pupular-names.txt

import sys
def tub_to_apace(file_name):
    res = []
    with open(file_name, "r") as f:
        for line in f:
            res.append(line.replace("\t", " "))
    return "".join(res)

if __name__ == "__main__":
    fn = sys.argv[1]
    print(tub_to_apace(fn))
