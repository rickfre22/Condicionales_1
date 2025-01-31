# Solicitar tiempo al usuario con un mensaje atractivo
tiempo = int(input("✨ Introduzca el tiempo (en segundos): "))

# Calcular el valor final basado en el tiempo
if tiempo <= 300:
    valor_final = 300
else:
    valor_final = 30 + 50 * (tiempo - 3)

# Aumentar el valor de a 50 si el tiempo es mayor a 3
if tiempo > 3:
    valor_final += 50 * (tiempo - 3)

# Imprimir el valor final con estilo
print(f"🌟 Valor final: {valor_final} 🌟")

