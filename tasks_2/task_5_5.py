import json

MENU = {'1': "Открыть файл",
        '2': "Просмотр характеристик в коммутаторе",
        '3': "Вывод данных по параметрам",
        '4': "Добавление значения",
        '5': "Удаление значения",
        '6': "Сохранить файл",
        'menu': "Меню",
        'exit': "Вывод"}

switchs = None


# Открываем файл
def open_json():
    with open('data.json', 'rt', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(f"Файл открыт. Строк: {len(data)}")
    return data


# Просмотр характеристик в коммутаторе
def show_data(data):
    print('Список коммутаторов')
    for k in data.keys():
        print(k)
    com = input("Введите название коммутатора:")
    if com in data.keys():
        print("Список характеристик:")
        for k, v in data[com].items():
            print(f"{k}: {v}")
        else:
            print(f"Коммутатора '{com}' нет в списке.")


# Вывод данных по параметрам
def param_show(data):
    print("Список коммутаторов:")
    print('\t'.join([k for k in data.keys()]))
    print('_________________________')
    print("Список параметров:")
    first_key = list(data.keys())[0]
    print('\n'.join([k for k in data[first_key]]))
    print('_________________________')
    com = input('Введите название коммутатора:')
    param = input('Введите название параметра:')
    try:
        print(data[com][param])
    except Exception as e:
        print(f"Ошибка при значения: {e}")


# Добавление значения
def add_new_switch(data):
    title = input("Название нового коммутатора:")
    pt = input("product Title:")
    mbps = input("10/100Mbps:")
    capacity = input("Forwarding capacity:")
    db = input("Data buffering:")
    fc = input("902.3 flow control:")
    mac = input("MAC address:")
    en = input("enclous materials:")
    gree = input("greennet:")
    warr = input("warranty:")
    new_switch = {title: {"product Title": pt,
                          "10/100Mbps": mbps,
                          "Forwarding capacity": capacity,
                          "Data buffering": db,
                          "902.3 flow control": fc,
                          "MAC address": nac,
                          "enclous materials": em,
                          "greennet": gree,
                          "warranty": warr
                          }}
    data = data | new_switch
    return data


# Удалить данные об устройстве
def delete_switch(data):
    print("Список коммутаторов:")
    print('\t'.join([k for k in data.keys()]))
    com = input("Введите название коммутатора:")
    try:
        del data[com]
    except Exception as e:
        print(f"Не удалось удалить {e}")
    print('Данные удалены.')


# Сохранение в файл
def save_json(data):
    with open('data.json', 'wt', encoding="utf-8") as f_out:
        json.dump(data, f_out)
    print("Данные сохранены!")


for k, v in MENU.items():
    print(f"{k} - {v}")

while True:
    comand = input(">> ")
    if comand == '1':
        switchs = open_json()
    elif comand == '2':
        show_data(switchs)
    elif comand == '3':
        param_show(switchs)
    elif comand == '4':
        switchs == add_new_switch(switchs)
    elif comand == '5':
        delete_switch(switchs)
    elif comand == '6':
        save_json(switchs)
    elif comand == 'menu':
        for k, v in MENU.items():
            print(f"{k} - {v}")
    elif comand == 'exit':
        break
