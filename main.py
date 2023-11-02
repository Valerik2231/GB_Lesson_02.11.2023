
phonebook = []
phbExit = False

def startPhonebook():
    phonebook = readTxt()

    while not phbExit:
        choise = startmenu()
        if(choise == 1):
            hpbPrint(phonebook)
        elif(choise ==2):
            phonebook.append(AddContact())
        elif(choise == 3):
            findeItems = FindeByName(phonebook)
            print(findeItems)
            pass
        elif choise == 4:
            findeItems = FindeByLastname(phonebook)
            print(findeItems)
            pass
        elif choise == 5:
            writetxt("phonebook.csv", book=phonebook)
        elif choise == 6:
            ChangeItem(phonebook)
        elif choise == 7:
            removeItem(phonebook)
        elif choise == 8:
            pass
        else:
            pass




def startmenu():
    print("\n")
    print("1. Расспечатать телефонный спраочник")
    print("2. Добавить запись")
    print("3. Поиск по имени")
    print("4. Поиск по фамилии")
    print("5. Выйти и сохранить")
    print("6. Изменить запись")
    print("7. Удалить запись")
    return int(input("Введите число: "))

def hpbPrint(phonebook):
    print("Имя \t Фамилия \t Номер телефона")
    i = 1
    for line in phonebook:
        values = list(line.values())
        print(i, values)
        i+=1

def AddContact():
    fields = ["Фамилия", "Имя", "Номер"]
    name = input("Введите имя: ")
    lastname = input("введите фамилию: ")
    phonenumber = input("Введите номер телефона: ")
    values = [name, lastname, phonenumber]
    return dict(zip(fields, values))
def FindeByName(book):
    name = input("Введите искомое имя: ")
    result = []
    for i in book:
        keyname = i.get("Имя")
        #print(name in keyname)
        if(name in keyname.lower()):
            result.append(i)
    return result

def FindeByLastname(book):
    lastname = input("Введите искомое имя: ")
    lastname.lower()
    result = []
    for i in book:
        keyname = i.get("Имя")
        #print(lastname in keyname)
        if (lastname in keyname.lower()):
            result.append(i)
    return result
    pass

def ChangeItem(book):
    number = int (input("Введите номер записи: "))
    number-=1


    if(number>=0 and number < len(book)):
        item = book[number]
        name = input("Введите имя: ")
        lastname = input("введите фамилию: ")
        phonenumber = input("Введите номер телефона: ")
        item["Имя"] = name
        item["Фамилия"] = lastname
        item["Номер"] = phonenumber
        print("Запись обновлена")
    else:print("Такой записи не существует")


def removeItem(book):
    number = int(input("Введите номер записи: "))
    number -= 1

    if (number >= 0 and number < len(book)):
        book.pop(number)
        print("запись успешно удалена")
    else:print("Такой записи не существует")


def readTxt(filename = "phonebook.csv"):
    phoneBook = []
    fields = ["Фамилия", "Имя", "Номер"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            phoneBook.append(dict(zip(fields, line.split(","))))
    return phoneBook
def writetxt(filename,book):


    with open(filename, "w", encoding="utf-8") as phb:
        result = []
        for item in book:
            lastname=item.get("Имя")
            name=item.get("Фамилия")
            number=item.get("Номер")
            descr =item.get("Описание")
            phb.write(lastname +","+name +","+ number + "\n")

    exit()



startPhonebook()