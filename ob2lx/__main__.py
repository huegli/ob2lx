import fileinput

from ob2lx.ob2lx import convert_l2o

if __name__ == "__main__":
    for line in fileinput.input(inplace=True):
        print(convert_l2o(line), end="")
