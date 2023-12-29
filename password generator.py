#codsoft
#password generator

import random
import array
MAX_LEN =10

d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

s= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
COMBINED_LIST = d+ upcase + lower + s
rand_digit = random.choice(d)
rand_upper = random.choice(upcase)
rand_lower = random.choice(lower)
rand_symbol = random.choice(s)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for adi in range(MAX_LEN - 6):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for adi in temp_pass_list:
    password = password + adi

# print out password
print(password)
