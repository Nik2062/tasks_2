interface = input("Введите тип и номер интерфейса: ")
Port = {
    "Fa0/1": "Sector-1 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/2": "Sector-2 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/3": "Sector-3 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/4": "notconnect 1 auto auto 10/100BaseTX",
    "Fa0/5": "port connected 100 a-full a-100 10/100BaseTX",
    "Fa0/6": "connected trunk full 100 10/100BaseTX",
    "Fa0/7": "disabled 100 auto auto 10/100BaseTX"
}
print(f'{interface} {Port[interface]}')
