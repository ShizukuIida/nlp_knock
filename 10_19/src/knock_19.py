#python knock_19.py ../data/popular-names.txt
#cut -f 1 popular-names.txt | sort | uniq -c | sort -k 1 -n -r | rev | cut -f 1 -d ' ' | rev | tr '\n' ','

import sys
import collections

def col1_frequency(file):
    with open(file, "r") as f:
        words = [line.split('\t')[0] for line in f.readlines() if line != '']

    return collections.Counter()

if __name__ == "__main__":
    file = sys.argv[1]
    print([i[0] for i in col1_frequency(file).most_common()])