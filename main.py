import os


def get_file_contents(filename):
    result = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def categorize_lyrics(lines):
    data = {}
    current_key = None
    for line in lines:
        if line.startswith("["):
            line_key = line.replace("[", "").replace("]", "")
            line_key_parts = line_key.split(":")
            if len(line_key_parts) == 2:
                line_key = line_key_parts[1]
            if line_key not in data.keys():
                data[line_key] = []
            current_key = line_key
        elif line == "":
            current_key = None
            print("found blank line")
        else:
            data[current_key].append(line)
    return data


def main():
    filename = "data.txt"
    lines = get_file_contents(filename)
    result = categorize_lyrics(lines)
    for k, v in result.items():
        print(k)


if __name__ == "__main__":
    main()
