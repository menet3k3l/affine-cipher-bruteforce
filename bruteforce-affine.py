from nostril import nonsense


# Iterative Algorithm (xgcd)
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = iterative_egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m


ct = input("CT: ")
ct_numbers = []

for letter in ct:
    number = ord(letter) - 65
    ct_numbers.append(number)

a_inv = []
b = []

for i in range(26):
    b.append(i)

for i in range(1,26,2):
    inv = modinv(i,26)
    if inv is not None:
        a_inv.append(inv)

pt = ""

for i in b:
    for j in a_inv:
        for number in ct_numbers:
            if number >= 0:
                pt_letter = (j*(number-i)) % 26 
                pt += str(chr(pt_letter+65))
            else:
                pt += " "
        if not nonsense(pt):
            print("PT: {}  ->    A_inv: {}, B: {}".format(pt,j,i))
        pt = ""
