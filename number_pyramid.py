# С Булева променлива

# number = int(input())
# counter = 1
# all_is_printed = False
# for row in range(1, number + 1):
#     for column in range(1, row + 1):
#         print(counter, end = " ")     #end = "\" като ентър, преминава на нов ред
#         counter += 1
#         if counter > number:
#             all_is_printed = True
#             break
#     if all_is_printed:
#         break
#     print()   # отпечатва на нов ред


# Без Булева променлива

number = int(input())
counter = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end = " ")     #end = "\" като ентър, преминава на нов ред
        counter += 1
        if counter > number:
            break
    if counter > number:
        break
    print()   # отпечатва на нов ред
