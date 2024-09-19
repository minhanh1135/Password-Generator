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



def modify_password_simple(pwd):
    # Thêm số vào cuối
    pwd += str(random.randrange(0, 10))
    
    # Thêm ký tự đặc biệt vào cuối
    pwd += random.choice(['!', '@', '#', '$'])
    
    # Thêm chữ hoa vào cuối
    pwd += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Thêm chữ số
    pwd += random.choice("0123456789")
    
    # Đảm bảo độ dài ít nhất 10 ký tự
    while len(pwd) < 10:
        pwd += random.choice("abcdefghijklmnopqrstuvwxyz")

    return pwd



def modify_existing_password(pwd):
    # Kiểm tra các điều kiện hiện tại của mật khẩu
    _, wcontinue = valid_password(pwd=pwd, show_warning=False)

    # Danh sách các ký tự cần thêm vào
    additions = ""

    # Thêm số nếu chưa có
    if not any(char.isdigit() for char in pwd):
        additions += str(random.randrange(0, 10))

    # Thêm ký tự đặc biệt nếu chưa có
    if not any(char in ['!', '@', '#', '$'] for char in pwd):
        additions += random.choice(['!', '@', '#', '$'])

    # Thêm chữ hoa nếu chưa có
    if not any(char.isupper() for char in pwd):
        additions = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + additions

    # Đảm bảo độ dài ít nhất 10 ký tự
    while len(pwd + additions) < 10:
        additions += random.choice("abcdefghijklmnopqrstuvwxyz")

    # Trả về mật khẩu đã được chỉnh sửa mà không chèn giữa, chỉ thêm vào đầu/cuối
    return additions + pwd
