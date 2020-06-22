import csv


def readers(file):
    with open(file, 'r') as f:
        data = f.readlines()
        for line in data:
            print(line)


def saver(file, data, position=None):
    if position:
        with open(file, "r") as infile:
            reader = list(csv.reader(infile))
            reader.insert(position, data)

        with open(file, 'w') as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)
    else:
        with open(file, 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data)


def remover(file, position=None):
    lines = list()

    with open(file, "r") as infile:
        reader = csv.reader(infile)

        for key, row in enumerate(reader):
            if key != position:
                lines.append(row)

    with open(file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines[:-1]) if position is None else writer.writerows(lines)


