import string
import collections
import csv


def write_csv(filename, key, counter):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow([key, ""])
        for word, amount in counter.most_common():
            writer.writerow([word, amount])


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
        else:
            data[current_key].append(line)
    return data


def count_words(verse_lines):
    counter = collections.Counter()

    for line in verse_lines:
        for word in line.split(" "):
            word = "".join(c for c in word if c not in string.punctuation)
            counter[word.lower()] += 1
    return counter


def main():
    filename = "data.txt"
    lines = get_file_contents(filename)
    result = categorize_lyrics(lines)
    data = {}
    for k, v in result.items():
        data[k] = count_words(v)

    for k, v in data.items():
        write_csv("Yah-Yah_{}.csv".format(k), k, v)


if __name__ == "__main__":
    main()
