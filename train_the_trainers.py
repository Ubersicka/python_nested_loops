number_of_juries = int(input())
name_of_presentation = input()
avarage_score = 0
count_score = 0
while name_of_presentation != "Finish":
    current_score = 0
    for juries in range(number_of_juries):
        current_score += float(input())
    print(f'{name_of_presentation} - {current_score / number_of_juries:.2f}.')
    count_score += 1
    avarage_score += current_score / number_of_juries
    name_of_presentation = input()
print(f"Student's final assessment is {avarage_score / count_score:.2f}.")
