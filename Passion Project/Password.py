def first():
    global filepath
    filepath = 'Login.txt'

def n_user():
    while True:
        flg = False
        user = input("Enter New Username (4 Characters): ")
        user = user.strip()

        with open(filepath, 'r') as f:
            for i in f:
                login_info = i.strip().split(',')

                if user == login_info[1]:
                    print('Error: Username Already In Use\n')
                elif len(user) < 4:
                    print("Error: Not Enough Characters\n")
                else:
                    print("Username Accepted\n")
                    pass_w = input("Enter New Password (8 Characters): ")

                    if len(pass_w) < 8:
                        print("Error: Not Enough Character\n")
                    else:
                        con_p_word = input("Enter Password Again: ")

                        if con_p_word == pass_w:
                            flg = True
                            sec = input('\nEnter Security Question: ')
                            ans = input('Enter Answer: ')

        if flg:
            print('\nAccount Created\n\n')
            with open(filepath, 'w') as f:
                pass_w = pass_w.strip()
                f.write('True')
                f.write(',')
                f.write(user)
                f.write(',')
                f.write(pass_w)
                f.write(',')
                f.write(sec)
                f.write(',')
                f.write(ans)
                f.write('\n')
                break

    o_user()


def f_pass():
    f = open(filepath, 'r')
    for i in f:
        q = i.strip().split(',')
        ans1 = input(f'{q[3]}?\n')
        if ans1 == q[4]:
            pass
        else:
            print('Wrong Answer')
            quit()
        user1 = q[1]
        pass_w1 = q[2]
        sec1 = q[3]
        ans1 = q[4]
    f.close()


    file = open(filepath, 'w')
    file.write('False')
    file.write(',')
    file.write(user1)
    file.write(',')
    file.write(pass_w1)
    file.write(',')
    file.write(sec1)
    file.write(',')
    file.write(ans1)
    file.write('\n')
    file.close()
    print('\n')
    second()


def o_user():
    while True:
        user = input('Enter Username (Forget to reset): ').strip()

        if user.lower() == 'forget':
            f_pass()
        else:
            with open(filepath, 'r') as f:
                for line in f:
                    login = line.strip().split(',')
                    if user == login[1]:
                        ps_word = input('Enter your password: ').strip()
                        if ps_word == login[2]:
                            print('Login successful\n')
                            return True
                        else:
                            print('Incorrect password\n')
                    else:
                        print('Username does not exist\n')

def second():
    with open(filepath, 'r') as f:
        for i in f:
            conf = i.strip().split(',')
            if conf[0] == 'True':
                if o_user():
                    return True
            else:
                n_user()
