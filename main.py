import os


def get_file_contents(filename):
    result = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def main():
    filename = "data.txt"
    lines = get_file_contents(filename)
    print(lines)


if __name__ == "__main__":
    main()
