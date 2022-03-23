#python python knock_15.py ../data/popular-names.txt 50
#split -n 50 ../data/popular-names.txt
import sys

def split_file(file, n):
    with open(file, 'r') as f:
        lines = [line.replace("\n", "") for line in f.readlines()]

    return ["\n".join(lines[i:i+n]) for i in range(0, len(lines), n)]

if __name__ == "__main__":
    file, n = sys.argv[1], int(sys.argv[2])
    print("\n\n".join(split_file(file, n)))
