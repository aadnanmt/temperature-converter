def fahrenheit_to_kelvin(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return kelvin

if __name__ == "__main__":
    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    suhu_kelvin = fahrenheit_to_kelvin(suhu_fahrenheit)
    print(f"Hasil: {suhu_fahrenheit} °F sama dengan {suhu_kelvin:.2f} K")