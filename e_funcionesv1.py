print("Manejo de funciones v1")
def hola_mundo():
    print("hola aqui estoy dentro de una funcion")

hola_mundo()

def mensa(msg):
    print(msg)

mensa("hola whatsapp")
mensa("el profe me sorprendio enviando mensajes")

def escribenc(nom,apll):
    print(nom,apll)
    print(f"Tu nombre completo es: {nom} {apll}")

escribenc("Pingu","Castañeda Chairez")

print("Funciones que regresan valores")

def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de:",s
print(suma2numeros(7,3))
print(suma2numeros(15,45))