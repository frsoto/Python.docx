def di_hola():
    print("Hola")

#%%
f1 = di_hola()  # Llama a la función
f2 = di_hola    # Asigna a f2 la función

#%%
print(f1)  # None       (di_hola no devuelve nada)
print(f2)  # <function di_hola at 0x1077bf158>

#%%
f1()       # Error! No es válido
f2()       # Llama a f2, que es di_hola()

#%%
del f2      # Borra el objeto que es la función
f2()      # Error! Ya no existe

#%%
di_hola()  # Ok. Sigue existiendo
