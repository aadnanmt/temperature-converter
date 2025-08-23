def fahrenheit_to_celsius(fahrenheit: float):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

if __name__ == "__main__":
    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    suhu_celsius = fahrenheit_to_celsius(suhu_fahrenheit)
    print(f"Hasil: {suhu_fahrenheit} °F sama dengan {suhu_celsius:.2f} °C")