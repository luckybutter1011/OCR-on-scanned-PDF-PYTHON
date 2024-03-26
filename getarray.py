import os

qty_array = []
itemcode_array = []

with open('extract/text_5.txt', 'r') as file:
    lines = file.readlines()
    
    # Delete the empty line and the line containing 'QTY'
    lines_qty = [line for line in lines if line.strip() and 'QTY' not in line]
    
    for line in lines_qty:
        line_split = line.split()
        
        if len(line_split) > 1:  # Check if the split line has more than one element
            itemcode_array.append(line_split[0])
            qty_array.append(line_split[1])
        
        if len(line_split) ==1 :  # Handle the case where line_split has only one element
            if(line_split[0]).isdigit():
                itemcode_array.append("")
                qty_array.append(line_split[0])  # Merge the string into the last itemcode_array
            else:
                itemcode_array[-1] += line_split[0]

# Write the qty_array and itemcode_array to files
with open("variable/qty.txt", 'w') as output:
    for qty in qty_array:
        output.write(qty + "\n")

with open("variable/itemcode.txt", 'w') as output:
    for itemcode in itemcode_array:
        output.write(itemcode + "\n")