import random

LOWERCASE_A_ASCII_NUMBER = 97
UPPERCASE_A_ASCII_NUMBER = 65

def get_number():
    return int(input("What number do you want:"))

print('''What kinda password do you want?
1) Weak
2) Moderate
3) Strong
4) Very Strong
''')

number = get_number()

def shuffle(ls: list):
    copy = ls.copy()
    length = len(ls)

    last_index = length-1

    while last_index > 0:
        random_number = random.randint(0,last_index - 1)
        temp = copy[random_number]
        copy[random_number] = copy[last_index]
        copy[last_index] = temp
        last_index-=1

    return copy

r2 = [1,2,3,4,5,6]

def false_or_true():
    return random.randint(0,10) > 5

def generateRandomChar(is_uppercase = False):
    selected_ascii = UPPERCASE_A_ASCII_NUMBER if is_uppercase else LOWERCASE_A_ASCII_NUMBER
    
    # 25 added because we want the range to be a - z
    return chr(random.randint(selected_ascii,selected_ascii+25))

def generate_random_number():
    return str(random.randint(0,9))

def generate_random_special_character():
    ls = [33,35,36,37,38]

    return chr(ls[random.randint(0,len(ls)-1)])

def generate_weak_password():
    password = ""

    for i in range(8):
        password = password + generateRandomChar()

    return "".join(shuffle([x for x in password]))

def generate_moderate_password():
    password = generateRandomChar() + generateRandomChar(True)

    for i in range(6):
        password = password + generateRandomChar(false_or_true())
    return "".join(shuffle([x for x in password]))

def generate_strong_password():
    password = generateRandomChar() + generateRandomChar(True) + generate_random_number()

    for i in range(5):
        password +=  generate_random_number() if false_or_true() else generateRandomChar(false_or_true())
    
    return "".join(shuffle([x for x in password]))

def generate_very_strong_password():
    password = generateRandomChar() + generateRandomChar(True)

    for i in range(3):
        password += generateRandomChar(false_or_true)

    password += generate_random_number() + generate_random_number()
    password += generate_random_special_character()

    return "".join(shuffle([x for x in password]))

match number:
    case 1:
        print(generate_weak_password())
    case 2:
        print(generate_moderate_password())
    case 3:
        print(generate_strong_password())
    case 4:
        print(generate_very_strong_password())