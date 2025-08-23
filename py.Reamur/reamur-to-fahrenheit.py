def reamur_to_fahrenheit(reamur: float):
    
    fahrenheit = (reamur * 2.25) + 32
    return fahrenheit

if __name__ == "__main__":
    suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
    suhu_fahrenheit = reamur_to_fahrenheit(suhu_reamur)
    print(f"Hasil: {suhu_reamur} °R sama dengan {suhu_fahrenheit:.2f} °F")