a = 24
b = 18

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

def LCM(a, b):
    return a * b // GCD(a, b)


GCD_result = GCD(a, b)
LCM_result = LCM(a, b)
print("GCD:", GCD_result)
print("LCM:", LCM_result)