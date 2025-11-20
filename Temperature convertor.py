
#Define convertors
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 273.15) * 5/9 + 32

#Write temperature convertor
def main():
    while True:
        print('Temperature convertor')
        print('1. Celsius to Fahrenheit')
        print('2. Fahrenheit to Celsius')
        print('3. Kelvin to Fahrenheit')
        print('4. Kelvin to Celsius')
        print('5. Celsius to Kelvin')
        print('6. Fahrenheit to Kelvin')
        print('7. Quit')

        choice = input('Enter your choice: ')
        if choice == '1':
            c = float(input('Enter temperature in Celsius: '))
            print(f'{c}°C = {celsius_to_fahrenheit(c):.2f}°F')
        elif choice == '2':
            f = float(input('Enter temperature in Fahrenheit: '))
            print(f'{f}°F = {fahrenheit_to_celsius(f):.2}°C')
        elif choice == '3':
            k = float(input('Enter temperature in Kelvin: '))
            print(f'{k}K = {kelvin_to_fahrenheit(k):.2}°F')
        elif choice == '4':
            k = float(input('Enter temperature in Kelvin: '))
            print(f'{k}K = {kelvin_to_celsius(k):.2}°C')
        elif choice == '5':
            c = float(input('Enter temperature in Celsius: '))
            print(f'{c}°C = {celsius_to_kelvin(c):.2}K')
        elif choice == '6':
            f = float(input('Enter temperature in Fahrenheit: '))
            print(f'{f}°F = {fahrenheit_to_kelvin(f):.2}K')
        elif choice == '7':
            print('Quit')
            break
        else:
            print('Invalid choice')
#Run it
main()