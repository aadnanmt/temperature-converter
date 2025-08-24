def fahrenheit_to_reamur(fahrenheit: float):
    reamur = (fahrenheit - 32) * 4/9
    return reamur

if __name__ == "__main__":
    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    suhu_reamur = fahrenheit_to_reamur(suhu_fahrenheit)
    print(f"Hasil: {suhu_fahrenheit} °F sama dengan {suhu_reamur:.2f} °R")