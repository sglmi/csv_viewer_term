import csv


# TODO:
# Distribute each cell equally in the length of the row.


def read_data(filename):
    with open(filename, "r") as csv_file:
        return list(csv.reader(csv_file))


def display(data):
    output = ""
    lines = []
    lengths = []
    biggest_len = 0
    for row in data:
        # clean white space around row item then join them with pipe symbole.
        line = " | ".join(item.strip() for item in row)
        line = f"| {line} |"
        lines.append(line)
        lengths.append(len(line))

    biggest_len = max(lengths)
    for line in lines:
        out = "".join(line) + "\n" + "-" * biggest_len
        print(out)
    # line += "-" * biggest_length
    # output += "\n" + line

    print(output)


if __name__ == "__main__":
    data = read_data("habit_track.csv")
    display(data)
