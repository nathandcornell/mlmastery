#! python3

# Example of integer encoding string class values
from csv import reader

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)

        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique_values = set(class_values)
    int_values = dict()

    for i, value in enumerate(unique_values):
        int_values[value] = i

    for row in dataset:
        row[column] = int_values[row[column]]

    return int_values
    

# Load iris dataset
filename = 'iris.csv'
dataset = load_csv(filename)

print('Loaded data file {0} with {1} rows and {2} columns'.format(
    filename, len(dataset), len(dataset[0])))
print('First row: {0}'.format(dataset[0]))

# Convert string columns to float
for i in range(4):
    str_column_to_float(dataset, i)

# convert class column to int
lookup = str_column_to_int(dataset, 4)
print('First row, revisited: {0}'.format(dataset[0]))
print(lookup)
