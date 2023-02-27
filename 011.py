def decorador(func):
    def envoltorio_func(a, b):
        print("Decorador antes de llamar a la función")
        c = func(a, b)
        print("Decorador después de llamar a la función")
        return c
    return envoltorio_func

def suma(a, b):
    print("Dentro de suma")
    return a + b

# Nueva funcion decorada
funcion_decorada = decorador(suma) # decoré a suma

funcion_decorada(5, 8)
