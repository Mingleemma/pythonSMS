from openpyxl import load_workbook

# path to Excel Sheet
filepath = "test.xlsx"

# column to Read from
column = "A"  # suppose it is under "A"

# number of cols to get
length = 3

workbook = load_workbook(filename=filepath, read_only=True)
worksheet = workbook.active  # we will get the active worksheet

phone_numbers = []
for i in range(length):
    cell = "{}{}".format(column, i + 1)
    number = worksheet[cell].value
    if number != "" or number is not None:
        phone_numbers.append(str(number))

print(phone_numbers)