#python python knock_15.py ../data/popular-names.txt 50
#tail -n 50 ../data/popular-names.txt
import sys

def tail(file_name, n):
    with open(file_name, "r") as f:
        res = [line for line in f.read().split("\n") if line != ''][-n:]
    return "\n".join(res)

if __name__ == "__main__":
    file, n = sys.argv[1], int(sys.argv[2])
    print(tail(file, n))
