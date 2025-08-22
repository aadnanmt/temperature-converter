def kelvin_to_fahrenheit(kelvin: float):
    return (kelvin - 273.15) * 1.8 + 32

if __name__ == "__main__":
    suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))
    suhu_fahrenheit = kelvin_to_fahrenheit(suhu_kelvin)
    print(f"Hasil: {suhu_kelvin} K sama dengan {suhu_fahrenheit:.2f} °F")