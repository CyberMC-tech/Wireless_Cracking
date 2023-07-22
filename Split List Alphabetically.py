# The location of the file.txt you want to split
LIST = ""

#Where you want to save the files
SAVE_LOCATION = ""

# Creating a list from the file
with open(LIST, "r") as n:
    FILE = n.read().splitlines()

list = []
ALP = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def start(let, list):
    new_list = []
    for i in list:
        if i.startswith(let):
            new_list.append(i)
    return new_list


def write_file(let, list):
    file = SAVE_LOCATION + "_" + let.upper() + ".txt"
    with open(file, "w") as f:
        for i in list:
            f.write(i + "\n")


for i in ALP:
    list = start(i, FILE)
    write_file(i, list)
