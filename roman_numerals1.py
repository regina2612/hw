
def write_roman(num):{

    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"
                    }

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])
Принимая его за спин:

num = 35
print write_roman(num)
# XXXV

num = 994
print write_roman(num)
# CMXCIV

num = 1995
print write_roman(num)
# MCMXCV

num = 2015
print write_roman(num)
# MMXV