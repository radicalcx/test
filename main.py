n = int(input('Введите число страниц: '))

count_paper = n // 4 + int(n % 4 != 0)

left = count_paper * 4 // 2
right = left + 1

if left > n:
    first_list = [[None, None]]
elif right > n:
    first_list = [[left, None]]
else:
    first_list = [[left, right]]

for i in range(count_paper - 1):
    left -= 2
    right += 2

    if left > n:
        first_list.append([None, None])
    elif right > n:
        first_list.append([left, None])
    else:
        first_list.append([left, right])

left = count_paper * 4 // 2 + 2
right = left - 3

if right > n:
    second_list = [[None, None]]
elif left > n:
    second_list = [[None, right]]
else:
    second_list = [[left, right]]

for i in range(count_paper - 1):
    left += 2
    right -= 2

    if right > n:
        second_list.append([None, None])
    elif left > n:
        second_list.append([None, right])
    else:
        second_list.append([left, right])

print(first_list)
print(second_list)
