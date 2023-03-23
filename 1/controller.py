import model

pb = model.PhoneBook(
    '1\contacts.txt')

while True:
    print(pb.main_menu())
    choice = int(input('выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(
                input('Введите индекс контакта, который необходимо изменить: '))
            name = input(
                'Введите имя или Enter, если изменение в имени не требуется: ')
            phone = input(
                'Введите телефон или Enter, если изменение в телефоне не требуется: ')
            comment = input(
                'Введите комментарий или Enter, если изменение в комментарии не требуется: ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(
                input('Введите индекс контакта, который необходимо удалить: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break
