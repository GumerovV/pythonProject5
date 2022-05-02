class Note:
    def __init__(self, name, surname, number, date):
        self.name = name
        self.surname = surname
        self.number = number
        self.date = date

    def __str__(self):
        return "{0.surname} {0.name}        {0.date[0]}.{0.date[1]}.{0.date[2]}       +{0.number}".format(self)

def find_person(list, numb):
    for i in range(len(list)):
        if list[i].number == numb:
            return print(list[i])
    return print("Number is not found!")

def print_list(list):
    for i in range(len(list)):
        print(list[i])

def sort_date(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i].date[2] > list[j].date[2]:
                list[i], list[j] = list[j], list[i]
            elif list[i].date[2] == list[j].date[2]:
                if list[i].date[1] > list[j].date[1]:
                    list[i], list[j] = list[j], list[i]
                elif list[i].date[1] == list[j].date[1]:
                    if list[i].date[0] > list[j].date[0]:
                        list[i], list[j] = list[j], list[i]

def create_list(list):
    print("         Введите информацию о восьми человек")
    for i in range(2):
        date = [0, 0, 0]
        print("Введите информацию о человеке №", i+1)
        print("Введите через пробел дату рождения (День/Месяц/Год):")
        while True:
            try:
                date[0], date[1], date[2] = map(int, input().split())
                break
            except ValueError:
                print("Введены некорректные данные!")
        print("Введите имя:")
        name = check_str()
        print("Введите фамилию:")
        surname = check_str()
        print("Введите номер телефона:")
        numb = check()
        person = Note(name, surname, numb, date)
        list.append(person)

def check():
    while True:
        try:
            x = int(input())
            return x
        except ValueError:
            print("Введены некорректные данные!")

def find_number(info):
    while True:
        print("Введите номер телефона человека, чтобы получить информацию о нем, или завершите программу, введя 0:")
        find_numb = check()
        if find_numb == 0:
            break
        find_person(info, find_numb)

def check_str():
        while True:
            x = input()
            if x and x.strip():
                return x
            else:
                print("Введены некорректные данные!")


def main():
    info = list()
    create_list(info)
    sort_date(info)
    print_list(info)
    find_number(info)

if __name__ == '__main__':
    main()