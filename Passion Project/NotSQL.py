from Basefile import i_hand, f_hand
from tabulate import tabulate
from Password import (
    first,
    second,
    n_user,
    o_user
)


l = []
dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}
dic5 = {}
x = 0
flag = False
n1 = ''
n2 = ''
n3 = ''
n4 = ''
n5 = ''
cl1 = []
cl2 = []
cl3 = []
cl4 = []
cl5 = []
big_flag = False


def head():
    head1 = ["Option No.", 'Function']
    func = [[1,'Create Table'], [2,'Delete Table'], [3,'Modify Table'], [4,'Query'], [5,'Print Table'], [6,'Help'], [7,'Quit']]
    txt = "  Not SQL  "
    txt = txt.center(31, '⌂')
    tx = '(Only Supports 5 Tables)'
    tx = tx.center(31, ' ')
    print(txt)
    print(tx)
    print(tabulate(func, headers=head1, tablefmt='pipe', colalign=('center', 'center')))

first()
if second():
    head()
    big_flag = True

if big_flag:
    while True:
        print('\n')
        inp = input('Enter Option No: ')
        if i_hand(inp):
            inp = int(inp)
            pass
        else:
            print("Wrong Input")
            continue

        if inp == 1:
            flag = True
            ip = input('How Many Tables (1 to 5): ')
            if i_hand(ip):
                ip = int(ip)
                pass
            else:
                print("Wrong Input")
                continue

            if ip == 1:
                n1 = input('Enter Table Name: ')
                a = input("How many Columns: ")
                b = input("How many Records: ")
                if i_hand(a) and i_hand(b):
                    a = int(a)
                    b = int(b)
                    pass
                else:
                    print("Wrong Input")
                    continue

                for j in range(1, a+1):
                    inp = input(f"Enter Name for Column {j}: ")
                    cl1.append(inp)

                for m in range(1, b+1):
                    for k in range(0, len(cl1)):
                        inpt = input(f"Enter Value {m} for {cl1[k]}: ")
                        l.append(inpt)
                    dic1[inp] = l
                    print(dic1)
                    l.clear()
                    print(dic1)
            elif ip in range(2,6):
                while ip != x:
                    a = input(f"How many Columns in Table {x+1}: ")
                    b = input(f"How many Records in Table {x+1}: ")
                    if i_hand(a) and i_hand(b):
                        a = int(a)
                        b = int(b)
                        pass
                    else:
                        print("Wrong Input")
                        continue

                    if x == 0:
                        n1 = input(f'Enter Table Name for Table {x + 1}: ')
                        for j in range(1, a + 1):
                            inp = input(f"Enter Name for Column {j} for Table {n1}: ")
                            cl1.append(inp)

                        for m in range(1, b + 1):
                            for k in range(0, len(cl1)):
                                inpt = input(f"Enter Value {m} for {cl1[k]}: ")
                                l.append(inpt)
                            dic1[m] = l
                            l.clear()
                    elif x == 1:
                        n2 = input(f'Enter Table Name for Table {x + 1}: ')
                        for j in range(1, a + 1):
                            inp = input(f"Enter Name for Column {j} for Table {n2}: ")
                            cl2.append(inp)

                        for m in range(1, b + 1):
                            for k in range(0, len(cl2)):
                                inpt = input(f"Enter Value {m} for {cl2[k]}: ")
                                l.append(inpt)
                            dic2[m] = l
                            l.clear()
                    elif x == 2:
                        n3 = input(f'Enter Table Name for Table {x + 1}: ')
                        for j in range(1, a + 1):
                            inp = input(f"Enter Name for Column {j} for Table {n3}: ")
                            cl3.append(inp)

                        for m in range(1, b + 1):
                            for k in range(0, len(cl3)):
                                inpt = input(f"Enter Value {m} for {cl3[k]}: ")
                                l.append(inpt)
                            dic3[m] = l
                            l.clear()
                    elif x == 3:
                        n4 = input(f'Enter Table Name for Table {x + 1}: ')
                        for j in range(1, a + 1):
                            inp = input(f"Enter Name for Column {j} for Table {n4}: ")
                            cl4.append(inp)

                        for m in range(1, b + 1):
                            for k in range(0, len(cl4)):
                                inpt = input(f"Enter Value {m} for {cl4[k]}: ")
                                l.append(inpt)
                            dic4[m] = l
                            l.clear()
                    elif x == 4:
                        n5 = input(f'Enter Table Name for Table {x + 1}: ')
                        for j in range(1, a + 1):
                            inp = input(f"Enter Name for Column {j} for Table {n5}: ")
                            cl5.append(inp)

                        for m in range(1, b + 1):
                            for k in range(0, len(cl5)):
                                inpt = input(f"Enter Value {m} for {cl5[k]}: ")
                                l.append(inpt)
                            dic5[m] = l
                            l.clear()
                    x += 1
            flag = True
        elif inp == 2 and flag:
            n = input("Enter Table Name To Delete: ")
            if n == n1:
                dic1.clear()
                n1 = 'null'
            elif n == n2:
                dic2.clear()
                n2 = 'null'
            elif n == n3:
                dic3.clear()
                n3 = 'null'
            elif n == n4:
                dic4.clear()
                n4 = 'null'
            elif n == n5:
                dic5.clear()
                n5 = 'null'
            else:
                print('Wrong Input')
                continue
        elif inp == 3 and flag:
            print("Coming Soon...")
            # i1 = input("Enter Table Name To Modify: ")
            # if i1 == n1:
            #
            # elif i1 == n2:
            #
            # elif i1 == n3:
            #
            # elif i1 == n4:
            #
            # elif i1 == n5:
            #
            # else:
            #     print('Wrong Input')
            #     continue
        elif inp == 4 and flag:
            print("Coming Soon...")
        elif inp == 5 and flag:
            while True:
                inp2 = input("Name The Table You Want To See ('q()' to Quit): ")
                if inp2 == n1:
                    kk = list(dic1.values())
                    print(dic1)
                    print(tabulate(kk, headers=cl1, tablefmt="grid"))
                elif inp2 == n2:
                    kk = list(dic2.values())
                    print(tabulate(kk, headers=cl2, tablefmt="grid"))
                elif inp2 == n3:
                    kk = list(dic3.values())
                    print(tabulate(kk, headers=cl3, tablefmt="grid"))
                elif inp2 == n4:
                    kk = list(dic4.values())
                    print(tabulate(kk, headers=cl4, tablefmt="grid"))
                elif inp2 == n5:
                    kk = list(dic5.values())
                    print(tabulate(kk, headers=cl5, tablefmt="grid"))
                elif inp2 == 'q()':
                    break
                else:
                    print("Wrong Input")
        elif inp == 6:
            head()
        elif inp == 7:
            quit()
        else:
            print('Please Create a Table First')