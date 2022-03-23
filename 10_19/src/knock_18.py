#python knock_18.py ../data/popular-names.txt
#sort -k 3 -n -r ../data/popular-names.txt
import sys

def col3_sort(file):
    with open(file, "r") as f:
        col3 = {int(line.split("\t")[2]):line.replace("\n", "").split("\t") \
                for line in f.readlines() if line != ""}
        return sorted(col3.items(), reverse=True)

if __name__ == "__main__":
    file = sys.argv[1]
    for i in col3_sort(file):
        print("\t".join(i[1]))