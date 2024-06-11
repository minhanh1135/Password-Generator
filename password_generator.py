import random

def replaceWithNumber(pwd, length_pwd):
    random_index = random.randrange(0, length_pwd)
    random_number = random.randrange(0, 9)
    return pwd[:(random_index)] + str(random_number) + pwd[(random_index + 1):]

def replaceWithSpecialNumber(pwd, length_pwd):
    special_number = ['!', '@', '#', '$']
    random_index = random.randrange(0, length_pwd)
    random_index_number = random.randrange(0, 4)
    return pwd[:(random_index)] + special_number[random_index_number] + pwd[(random_index + 1):]

def replaceWithUpper(pwd, length_pwd):
    random_index = random.randrange(0, length_pwd)
    return pwd[:(random_index)] + pwd[random_index].upper() + pwd[(random_index + 1):]