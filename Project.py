from tabulate import tabulate


def credit():
    global dic, head
    dic = {}
    n = int(input("Enter No of Values: "))

    for i in range(1, n+1):
        a = input(f"Enter Credit Card No. {i}: ")
        b = input(f"Enter {a}'s Mobile No.: ")
        print('\n')
        dic[i] = [a, b]

    data = list(dic.values())
    head = ["Credit Card No.", "Mobile No."]

    print('\n')
    print(tabulate(data, headers=head, tablefmt="pipe", colalign=('center', 'center')))
    print('\n\n')


def search():
    flag = True
    data1 = []
    while True:
        print('\n')
        fl = False
        if flag:
            n = input("Do You Want to Search(Y/N): ")
            n = n.lower()
            flag = False
        else:
            n = input("Continue Searching?(Y/N): ")
            n = n.lower()

        if n == 'y':
            print('\n')
            k = input("Enter Credit Card No to Be Searched: ")
            for i in dic:
                f = dic[i]

                if f[0] == k:
                    fl = True
                    data1 = [f]

            if fl:
                print(tabulate(data1, headers=head, tablefmt="pipe", colalign=('center', 'center')))
            else:
                print("No Value Matches")
        elif n == 'n':
            quit()
        else:
            print("Wrong Input")


def lit():
    global l
    n = int(input("Enter No Of Values: "))
    l = []
    for i in range(1, n+1):
        a = input(f"Enter Value {i}: ")
        l.append(a)


def pi_base():
    flg = False
    data = [
        [1, 'Append Element'],
        [2, 'Insert Element'],
        [3, 'Append List'],
        [4, 'Slice List'],
        [5, 'Delete Through Index'],
        [6, 'Delete Through Value'],
        [7, 'Sort (Ascend)'],
        [8, 'Sort (Descend)'],
        [9, 'Print List'],
        [10, 'Clear List'],
        [11, 'Quit']
    ]

    txt = "π-Base"
    txt = txt.center(41, '*')
    head1 = ['Function No.', 'Function Name']

    while True:
        print('\n\n')
        print(txt)
        print(tabulate(data, headers=head1, tablefmt='grid', colalign=('center', 'center')))

        print('\n')
        n = int(input('Enter Function No: '))

        if n == 1:
            print('\n')
            no = int(input('Enter No Of Values: '))
            for i in range(1, no+1):
                a = input(f'Enter Value {i}: ')
                l.append(a)
        elif n == 2:
            print('\n')
            no = int(input('Enter No Of Values: '))
            for i in range(1, no + 1):
                a = input(f'Enter Value {i}: ')
                b = int(input(f'Enter Index No for {a}: '))
                l.insert(b, a)
        elif n == 3:
            print('\n')
            flg = True
            no = int(input('Enter No Of Lists: '))
            ll = []
            for i in range(1, no + 1):
                print('\n')
                lb = int(input(f"Enter No Of Values In List {i}: "))
                for j in range(1, lb+1):
                    a = input(f'Enter Value {j}: ')
                    ll.append(a)
                l.append(str(ll))
                ll.clear()
        elif n == 4:
            print('\n')
            a = int(input('Enter First Index No.: '))
            b = int(input('Enter Second Index No.: '))
            c = int(input('Enter Step Value (Default = 1): '))
            print(l[a:b:c])
        elif n == 5:
            print('\n')
            no = int(input("Enter No Of Times: "))
            for i in range(1, no+1):
                a = int(input("Enter Index No: "))
                del l[a]
        elif n == 6:
            print('\n')
            no = input("Enter Value to Be Removed: ")
            na = input('Do You Want To Remove All Values(Y/N): ')
            na = na.lower()
            if no in l:
                if na == 'y':
                    while no in l:
                        l.remove(no)
                elif na == 'n':
                    ab = int(input('Enter No Of Times: '))
                    for k in range(0, ab):
                        l.remove(no)
                else:
                    print("Wrong Input")
            else:
                print("No Value In list")
        elif n == 7:
            if flg:
                print('\n')
                print("Cant Sort List With Nested List")
            else:
                l.sort()
        elif n == 8:
            if flg:
                print('\n')
                print("Cant Sort List With Nested List")
            else:
                l.sort(reverse=True)
        elif n == 9:
            print('\n')
            print(l)
        elif n == 10:
            flg = False
            l.clear()
        elif n == 11:
            quit()
        else:
            print("Wrong Input")

        while True:
            print('\n')
            ask = input('Do You Want To Continue(Y/N): ')
            ask = ask.lower()
            if ask == 'y':
                break
            elif ask == 'n':
                quit()
            else:
                print("Wrong Input")

while True:
    x = input("Credit or List?: ")
    x = x.lower()
    if x == 'credit':
        credit()
        search()
        quit()
    elif x == 'list':
        print('\n')
        lit()
        pi_base()
        quit()
    else:
        print("Wrong Input")
        print('\n')