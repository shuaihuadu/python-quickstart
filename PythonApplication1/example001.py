from math import cos, radians


def make_dot_string(x):
    rad = radians(x)
    numspace = int(20 * cos(rad) + 20)
    st = " " * numspace + "o"
    return st


def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)

main()        