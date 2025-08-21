def celsius_to_reamur(celcius: float):
    return celcius * 4/ 5


if __name__ == "__main__":
    suhu_celcius = float(input("Masukkan suhu dalam Celsius: "))
    suhu_reamur = celsius_to_reamur(suhu_celcius)
    print(f"Hasil: {suhu_celcius}°C sama dengan {suhu_reamur:.2f}°R")