
def enter_user():
    import datetime , time
    password = 'E4NF'
    enter_password = str(input('please enter password: '))
    if enter_password == password:
        time.sleep(2)
        print("done........")
    else:
        print("error 404 not found...")
        time.sleep(2)
        exit()
enter_user()

