def celsius_to_kelvin(celcius: float):
    return celcius + 273.15


if __name__ == "__main__":
    suhu_celcius = float(input("Masukkan suhu dalam Celsius: "))
    suhu_kelvin = celsius_to_kelvin(suhu_celcius)
    print(f"Hasil: {suhu_celcius}°C sama dengan {suhu_kelvin:.2f}°K")