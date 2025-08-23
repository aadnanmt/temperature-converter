def reamur_to_kelvin(reamur: float):
   
   
    celsius = reamur * 1.25
    kelvin = celsius + 273.15
    return kelvin
    
if __name__ == "__main__":
    suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
    suhu_kelvin = reamur_to_kelvin(suhu_reamur)
    print(f"Hasil: {suhu_reamur} °R sama dengan {suhu_kelvin:.2f} K")

