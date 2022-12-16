PC_Names= {
    "Bronze": {
        "OC": "Windows 11 Pro",
        "Processor": "Intel Core i5-10600KF",
        "RAM": "32768 MB",
        "Video card": "AMD Radeon RX 6700 XT 12 GB",
        "ROM": "1TB HDD Barracuda 7200prm",
        "PSU": "DeepCool PQ 750W",
        "Motherboard": "GIGABYTE Z590 GAMING X",
    },
    "Bomj": {
        "OC": "Windows 10 Home",
        "Processor": "AMD Ryzen 5 1600 six core",
        "RAM": "8192 MB",
        "Video card": "Nvidia GeForce GTX 1050 2G",
        "ROM": "480 GB SSD AData",
        "PSU": "Aerocool VX 450W",
        "Motherboard": "GIGABYTE B450M DS3H",
    },
    "UEPE_PC": {
        "OC": "Windows 11 Pro",
        "Processor": "AMD Ryzen 9 7950X",
        "RAM": "512 GB",
        "Video card": "Nvidia Geforce RTX 4090 24 GB",
        "ROM": "7680 GB Intel Optane D7-P5510",
        "PSU": "Thermaltake Toughpower TF1 1550W",
        "Motherboard": "ASUS ROG CROSSHAIR X670E HERO",
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")
print(PC_Names[device][parameter])