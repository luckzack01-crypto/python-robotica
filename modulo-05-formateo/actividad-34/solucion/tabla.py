ultrasonidos = 40
infrarrojos = 12
luz = 7

barra= "#" * (ultrasonidos // 5)
print(f"ultrasonidos: {ultrasonidos:.1f} {barra}")

barra = "#" * (infrarrojos // 5)
print(f"barra_infrarrojos {infrarrojos:.1f} {barra}")

barra_luz = "#" * (luz // 5)
print(f"barra_luz {infrarrojos:.1f} {barra}")