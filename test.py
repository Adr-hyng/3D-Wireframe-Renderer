from ast import literal_eval
with open("Plot/output.txt", "r") as f:
    line = f.read()
    print(type(line))
    print(literal_eval(line))