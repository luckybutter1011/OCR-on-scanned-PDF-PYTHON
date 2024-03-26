import re

length = 0

with open('extract/text_4.txt', 'r') as file4:
    qty_array = [line[:-1] for line in file4 if line.strip() and ("QTY" not in line)]
    length = len(qty_array)
    # print(qty_array)
    
with open('extract/text_1.txt', 'r') as file1:
    # description_string = file.read()
    description_array = [line[:-1] for line in file1 if line.strip() and ("NO\n" not in line and "DESCRIPTION" not in line)]

    ## split with "material" and merge
    merged_strings = []
    current_string = []
    materials = []
    for element in description_array:
        if "MATERIALS" in element:
            materials.append(element)
            if current_string: # If there's a string being merged, append it
                merged_strings.append(current_string)
                current_string = [] # Start a new string
        else:
            current_string.append(element)
    if current_string:
        merged_strings.append(current_string)

    print(merged_strings)
    