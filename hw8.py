# 1

numbers = [ 1, 4, 8, 10, 25 ]
new_numbers = [x * 10 for x in numbers if x % 2 == 0]
print(new_numbers)


# 2

menu = {
    'beefstrogonoff': 350,
    'burger': 200,
    'meatloaf': 500,
    'chicken pot pie': 400,
    'beefshteks': 650
}

new_menu = {
    'beefstrogonoff': 350,
    'burger': 200,
    'meatloaf': 500,
    'chicken pot pie': 400,
    'beefshteks': 650
}
new_menu = {k : (v + 50) for (k, v) in menu.items()}

print(new_menu) 

