import os
import re

qty_array = []
size_array = []
des_shop_array = []
des_field_array = []
length = 0

path = 'variable'
os.makedirs(path, exist_ok=True)

# Function to replace patterns in a string
def replace_patterns(s, patterns):
    for pattern, replacement in patterns.items():
        s = s.replace(pattern, replacement)
    return s

def replace_special_chars(text):
    pattern = r'-(?=—)'
    modified_text = re.sub(pattern, '', text)
    modified_text = re.sub('—', '-', modified_text)
    
    return modified_text

def get_itemcode_7000():
    try:
        with open('extract/text_4.txt', 'r') as file:
            lines = file.readlines()
            lines_cv = [line for line in lines if line.strip()]
            print(lines_cv)
            patterns = {'ss)': '5', 'rs)': '5', 'x)': '3'}
            temp_array = [replace_patterns(s, patterns) for s in lines_cv]
            print(temp_array)
            pattern = r'[^0-9/+\-x]+'
            modified_array = [re.sub(pattern, '', s) for s in temp_array]
            modified_array = modified_array[::-1]
            return modified_array
    except:
        return([])
    
def get_size_7000():
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
            return(len, temp_array)
            
    except:
        return(0, [])
    
# def des_combine_7000(content):

def get_des_7000(length):
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
        temp_array = temp_array[::-1]
        temp_array = [replace_special_chars(s) for s in temp_array]

        return (temp_array[:length], temp_array[length:])
    except:
        return([], [])

length, size_array = get_size_7000()
des_shop, des_field = get_des_7000(length)
qty_array = get_itemcode_7000()