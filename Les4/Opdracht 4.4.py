def new_password(oldpassword, newpassword):
    if oldpassword == newpassword or len(str(newpassword)) < 6: #Is het And of Or
        return 'False'
    else:
        return 'True'