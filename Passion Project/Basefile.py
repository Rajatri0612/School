def i_hand(n):
    try:
        int(n)
        return True
    except:
        return False

def f_hand(n):
    try:
        float(n)
        return True
    except:
        return False