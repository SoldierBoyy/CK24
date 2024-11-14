import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

newline = '\n'
delimeter_csv = ','
indent = 4

def task() -> None:
    with open(INPUT_FILENAME, "r", newline=newline) as input_file:
        reader = csv.DictReader(input_file, delimiter=delimeter_csv)
        reader_data = [row for row in reader]

        with open(OUTPUT_FILENAME, "w") as output_f:
            json.dump(reader_data, output_f, indent=indent)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
