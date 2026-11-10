def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a tu proyecto de Python."

def main():
    nombre = input("Escribe tu nombre: ")
    print(saludar(nombre))

if __name__ == "__main__":
    main()