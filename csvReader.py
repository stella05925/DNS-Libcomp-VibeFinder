import csv

class TextToCSV:
    def __init__(self, input_file, delimiter, output_file):
        self.input_file = input_file
        self.delimiter = delimiter
        self.output_file = output_file

    def convert(self):
        with open(self.input_file, 'r') as infile:
            lines = infile.readlines()

        data = [line.strip().split(self.delimiter) for line in lines]

        with open(self.output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(data)

        print(f"Conversion complete. CSV file saved as '{self.output_file}'")

class CSVToText:
    def __init__(self, input_file, delimiter, output_file):
        self.input_file = input_file
        self.delimiter = delimiter
        self.output_file = output_file

    def convert(self):
        with open(self.input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)
            data = list(reader)

        with open(self.output_file, 'w') as outfile:
            for row in data:
                outfile.write(self.delimiter.join(row) + '\n')

        print(f"Conversion complete. Text file saved as '{self.output_file}'")