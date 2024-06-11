def valid_password(pwd, show_warning=False):
    wlen = False
    if len(pwd) >= 10:
        wlen = True
    wupper_isupper = False
    wnumeric = False
    wspecial_number = False
    special_number = ["!", "?", "@", "#"]
    wcontinue = False

    for w in pwd:
        if w.isupper() == True:
            wupper_isupper = True
        if w in special_number:
            wspecial_number = True
        if w.isnumeric() == True:
            wnumeric = True

    if wlen == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain 10 words")
    if wspecial_number == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain a special number")
    if wnumeric == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain a number")
    if wupper_isupper == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain an upper case letter")

    return pwd, wcontinue