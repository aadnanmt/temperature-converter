def kelvin_to_reamur(kelvin: float):
    return (kelvin - 273.15) * 0.8

if __name__ == "__main__":
    suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))
    suhu_reamur = kelvin_to_reamur(suhu_kelvin)
    print(f"Hasil: {suhu_kelvin} K sama dengan {suhu_reamur:.2f} °R")