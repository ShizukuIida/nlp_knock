#python knock_17.py ../data/popular-names.txt
#cut -f 1 ../data/popular-names.txt | sort | uniq | tr '\n' ','
import sys

def col1_type(file):
    with open(file, "r") as f:
        col1 = [line.split("\t")[0] for line in f.readlines() if line != '']
        return {line for line in col1}

if __name__ == "__main__":
        file = sys.argv[1]
        print(col1_type(file))