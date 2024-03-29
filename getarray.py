import os
import re

qty_array = []
itemcode_array = []
size_array = []
des_shop_array = []
des_field_array = []

path = 'variable'
os.makedirs(path, exist_ok=True)

def get_itemcode():
    try:
        temp_array1 = []
        temp_array2 = []
        with open('extract/text_3.txt', 'r') as file:
            lines = file.readlines()
            # Delete the empty line and the line containing 'QTY'
            lines_qty = [line for line in lines if line.strip() and 'QTY' not in line]
    
            for line in lines_qty:
                line_split = line.split()
                
                if len(line_split) > 1:  # Check if the split line has more than one element
                    temp_array1.append(line_split[0])
                    temp_array2.append(line_split[1])
                
                if len(line_split) ==1 :  # Handle the case where line_split has only one element
                    if(line_split[0]).isdigit():
                        temp_array1.append("")
                        temp_array2.append(line_split[0])  # Merge the string into the last array
                    else:
                        temp_array1[-1] += line_split[0]
    except:
        return([], [])
    return (temp_array1, temp_array2)

def get_size():
    try:
        with open("extract/text_2.txt", "r") as file:
            lines = file.readlines()
            lines_cv = [line.replace("\n", "") for line in lines if line.strip()]
            pattern = r'^[^a-zA-Z].*$'
            return [line for line in lines_cv if re.match(pattern, line)]
    except:
        return([])
    
def des_combine(content):
    # Combine the seperated sentence in one for description
    try:
        temp_array = []
        lines = content.splitlines()
        lines = [line for line in lines if line.strip()]

        for line in lines:
            line_split = line.split()
                
            if len(line_split) > 1 :
                if re.match(r"^\d", line_split[0]):  # Check if the split line has more than one element
                    if re.match(r"^\d+(\.)?$", line_split[0]):
                        temp_array.append(' '.join(line_split[1:]))
                    else :
                        temp_array[-1] += " " + line
                else:
                    temp_array[-1] += " " + line

            if len(line_split) == 1 :  # Handle the case where line_split has only one element
                temp_array[-1] += " " + line
    except:
        return ([])

    return temp_array

def get_des():
    # Description with shop and field material
    try:
        with open("extract/text_1.txt", "r") as file:
            content_des = file.read()
        content_shop = re.search(r"SHOP MATERIAL(.*?)FIELD MATERIAL", content_des, re.DOTALL).group().strip()
        content_field = re.search(r"FIELD MATERIAL(.*)", content_des, re.DOTALL).group().strip()

        pattern = re.compile(r'^FLANGES.*$|^VALVES / IN-LINE ITEMS.*$|^PIPE.*$|^FITTINGS.*$|^SUPPORTS.*$|^GASKETS.*$|^BOLTS.*$|', re.MULTILINE)
        pattern_s = re.compile(r"SHOP MATERIAL.*?NO|FIELD MATERIAL", re.DOTALL) 

        content_shop_c = re.sub(pattern_s, "", content_shop) # divide the string into SHOP and FIELD
        content_shop_c1 = re.sub(pattern, "", content_shop_c) # delete the FLANGES VALUES PIPES
        # print(content_shop_c1)

        pattern_f = re.compile("FIELD MATERIAL.*?NO", re.DOTALL)

        content_shop_f = re.sub(pattern_f, "", content_field) # divide the string into SHOP and FIELD
        content_shop_f1 = re.sub(pattern, "", content_shop_f) # delete the FLANGES VALUES PIPES
        # print(content_shop_f1)
    except:
        return([], [])
    return (des_combine(content_shop_c1), des_combine(content_shop_f1))

# Initiate the value
des_shop_array, des_field_array = get_des()
itemcode_array, qty_array = get_itemcode()
size_array = get_size()

# Size array 
with open("variable/size.txt", "w") as file1:
    for line in size_array:
        file1.write(line + "\n")

# QTY array
with open("variable/qty.txt", 'w') as output:
    for qty in qty_array:
        output.write(qty + "\n")

# Itemcode array
with open("variable/itemcode.txt", 'w') as output:
    for itemcode in itemcode_array:
        output.write(itemcode + "\n")

# Descriptino shop array
with open("variable/des_shop.txt", 'w') as output:
    for des_shop in des_shop_array:
        output.write(des_shop + "\n")

# Descriptino shop array
with open("variable/des_field.txt", 'w') as output:
    for des_field in des_field_array:
        output.write(des_field + "\n")

