def kelvin_to_celsius(kelvin: float):
    return kelvin - 273.15

if __name__ == "__main__":
    suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))
    suhu_celcius = kelvin_to_celsius(suhu_kelvin)
    print(f"Hasil: {suhu_kelvin} K sama dengan {suhu_celcius:.2f} °C")