def celsius_ke_fahrenheit(celcius: float):
    return celcius * 9/5 + 32


if __name__ == "__main__":
    suhu_celcius = float(input("Masukkan suhu dalam Celsius:  "))
    suhu_fahrenheit = celsius_ke_fahrenheit(suhu_celcius)
    print(f"Hasil: {suhu_celcius}°C sama dengan {suhu_fahrenheit:.2f}°F")