def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


print("Temperaturumrechner")
print("1. Celsius zu Kelvin")
print("2. Celsius zu Fahrenheit")
print("3. Kelvin zu Celsius")
print("4. Kelvin zu Fahrenheit")
print("5. Fahrenheit zu Celsius")
print("6. Fahrenheit zu Kelvin")

option = int(input("Bitte wählen Sie eine der obigen Optionen (1-6): "))

temperature = float(input("Geben Sie die Temperatur ein: "))

if option == 1:
    converted_temp = celsius_to_kelvin(temperature)
    print(f"{temperature} °C entsprechen {converted_temp} K")
elif option == 2:
    converted_temp = celsius_to_fahrenheit(temperature)
    print(f"{temperature} °C entsprechen {converted_temp} °F")
elif option == 3:
    converted_temp = kelvin_to_celsius(temperature)
    print(f"{temperature} K entsprechen {converted_temp} °C")
elif option == 4:
    converted_temp = kelvin_to_fahrenheit(temperature)
    print(f"{temperature} K entsprechen {converted_temp} °F")
elif option == 5:
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"{temperature} °F entsprechen {converted_temp} °C")
elif option == 6:
    converted_temp = fahrenheit_to_kelvin(temperature)
    print(f"{temperature} °F entsprechen {converted_temp} K")
else:
    print("Ungültige Option. Bitte wählen Sie eine Zahl von 1 bis 6.")
