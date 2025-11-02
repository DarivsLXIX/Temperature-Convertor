
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print('Temperature converter')
        print('1. Celsius to Fahrenheit')
        print('2. Fahrenheit to Celsius')
        print('3. Quit')

        choice = input('Enter your choice (1, 2, 3): ')

        if choice == '1':
            c = float(input('Enter temperature in Celsius: '))
            print(f'{c}°C = {celsius_to_fahrenheit(c):.2f}°F')
        elif choice == '2':
            f = float(input('Enter temperature in Fahrenheit: '))
            print(f'{f}°F = {fahrenheit_to_celsius(f):.2f}°C')
        elif choice == '3':
            break
        else:
            print('Enter a valid choice')
main()




