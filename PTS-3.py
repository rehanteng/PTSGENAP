def suhu(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

hasil_konversi = suhu(30)

print(f"30°C sama dengan {hasil_konversi:.1f}°F")
