# for h in range (24):            #Изпринтира от 0 до 23
#     for m in range (60):            #Като приключат интерациите на вложения цикъл, се връща към 0
#         print(f'{h}:{m}')       # можем да сложим в {m:02d} 02d- за водеща 0-ла.. 01, 02, 03 вместо 1, 2, 3

# с булева променлива
# flag = False
# for i in range(n):
#     for j in range (n):
#         if condition:
#             flag = True
#             break
#     if flag:
#         break

# Първо вътрешния цикъл се извърта!

floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        print(f'{f}{r}', end=" ")    # end - пише ги на един ред,
--------------
# while True:
#     while True:  # Това е 2ри вложен цикъл
#         continue
#         break    # тези 3те команди работят само за 2рия вложен цикъл
#         pass
#     continue     # Тия 2те команди работят само за външния цикъл
#     break

number = 1
while True:
    while True:  # Това е 2ри вложен цикъл
        number += 1
        print(number)
    while number > 5:
        break
