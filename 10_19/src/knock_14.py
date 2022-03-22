#python knock_14.py ../data/popular-names.txt 5
#head -n 5 ../data/popular-names.txt 5
import sys

def head_text(file, n):
    with open(file, "r") as f:
        res = []
        for i, line in enumerate(f):
            if i == n:
                break
            res.append(line.replace('\n', ''))

    return res

if __name__ == "__main__":
    file, n = sys.argv[1], int(sys.argv[2])
    print("\n".join(head_text(file, n)))