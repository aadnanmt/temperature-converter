def reamur_to_celsius(reamur: float):
    
    celsius = reamur * 1.25
    return celsius

if __name__ == "__main__":
    suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
    suhu_celsius = reamur_to_celsius(suhu_reamur)
    print(f"Hasil: {suhu_reamur} °R sama dengan {suhu_celsius:.2f} °C")

