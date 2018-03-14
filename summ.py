numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ = 0
multi = 1
for number in numbers_list:
    summ = number+summ
    multi = number*multi
    print(f'summ = {summ}')
    print(f'multi = {multi}')
    