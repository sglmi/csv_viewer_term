import csv


def read_data(filename):
    with open(filename, "r") as csv_file:
        return list(csv.reader(csv_file))


def display(data):
    output = ""
    lines = []
    biggest_length = 0
    for row in data:
        # clean white space around row item then join them with pipe symbole.
        line = " | ".join(item.strip() for item in row)
        line = f"| {line} | \n"
        if len(line) > biggest_length:
            biggest_length = len(line)

        line += "-" * biggest_length
        output += "\n" + line

    print(output)


if __name__ == "__main__":
    data = read_data("habit_track.csv")
    display(data)
