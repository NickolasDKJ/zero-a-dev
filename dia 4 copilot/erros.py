try:
    numero = float(input("Digite um número: "))
    resultado = 10 / numero
    print("10 dividido por", numero, "=", resultado)
except ValueError:
    print("Isso não é um número!")
except ZeroDivisionError:
    print("Não da pra dividir por zero!")
finally:
    print("Programa finalizado.")
    