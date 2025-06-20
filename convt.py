def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print("🌡️ Welcome to Temperature Converter!")
print("Convert between Celsius (C), Fahrenheit (F), and Kelvin (K).")

while True:
    temp = input("\nEnter temperature (e.g., 100C, 212F, 300K or 'exit' to quit): ").strip().upper()
    
    if temp == 'EXIT':
        print("Thanks for using the converter. Goodbye!")
        break

    try:
        value = float(temp[:-1])
        scale = temp[-1]

        if scale == 'C':
            print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
            print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
        elif scale == 'F':
            print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
            print(f"{value}°F = {fahrenheit_to_kelvin(value):.2f}K")
        elif scale == 'K':
            print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
            print(f"{value}K = {kelvin_to_fahrenheit(value):.2f}°F")
        else:
            print("❌ Unknown temperature scale. Use C, F, or K.")
    except:
        print("❌ Invalid format. Please enter like 100C or 212F.")
