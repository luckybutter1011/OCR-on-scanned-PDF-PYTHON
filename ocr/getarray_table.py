import os
import re

qty_array = []
size_array = []
des_shop_array = []
des_field_array = []
length = 0

# Function to replace patterns in a string
def replace_patterns(s, patterns):
    for pattern, replacement in patterns.items():
        s = s.replace(pattern, replacement)
    return s

def replace_special_chars(text):
    pattern = r'-(?=—)'
    modified_text = re.sub(pattern, '', text)
    modified_text = re.sub('—', '-', modified_text)
    pattern_end = r'\)$'  # Pattern to remove ")" at the end of the string
    modified_text = re.sub(pattern_end, '', modified_text)
    
    return modified_text

def get_itemcode_table():
    try:
        with open('extract/text_4.txt', 'r') as file:
            lines = file.readlines()
            lines_cv = [line for line in lines if line.strip()]
            # print(lines_cv)
            patterns = {'ss)': '5', 'rs)': '5', 'x)': '3'}
            temp_array = [replace_patterns(s, patterns) for s in lines_cv]
            # print(temp_array)
            pattern = r'[^0-9/+\-x]+'
            modified_array = [re.sub(pattern, '', s) for s in temp_array]
            modified_array = modified_array[::-1]
            return modified_array
    except:
        return([])
    
def get_size_table():
    len = 0
    temp_array = []
    try:
        with open('extract/text_2.txt', 'r') as file:
            lines = file.readlines()
            lines_cv = [line.replace("\n", "") for line in lines if line.strip()]
            lines_data = lines_cv[::-1][1:]
            pattern1 = r'^[^a-zA-Z].*$'
            for line in lines_data:
                if re.match(pattern1, line):
                    len = len + 1
                else:
                    break
            temp_array = [line for line in lines_cv if re.match(pattern1, line)]
            pattern2 = r'[^0-9/+\-x]+'
            temp_array = [re.sub(pattern2, '', s) for s in temp_array]
            modified_lines = [ line.replace('9', '2') if line == '9' else line for line in temp_array ]
            return(len, modified_lines)
            
    except:
        return(0, [])
    
def get_des_table(length):
    temp_array = []
    temp = ''
    try:
        with open('extract/text_1.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():  # Check if the line is not empty
                    temp += line
                else:
                    temp_array.append(temp)
                    temp = ''
            temp_array.append(temp)
            temp = ''
        print(len(temp_array))
        print("--------------------------->")
        temp_array = temp_array[::-1]
        print(len(temp_array))
        temp_array = [replace_special_chars(s) for s in temp_array]

        return (temp_array[:length], temp_array[length:])
    except:
        return([], [])

length, size_array = get_size_table()
des_shop, des_field = get_des_table(length)
qty_array = get_itemcode_table()