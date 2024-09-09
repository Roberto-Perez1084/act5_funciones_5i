print("funciones creadas por el usuario")
print("Lista")
def milista():
    amigosL=["Chamba","Milic","Robertote"]
    for yo in amigosL:
        print(yo)
milista()
print("")
print("Tupla")
def mitupla():
    amigosT=("Chamba","Milic","Robertote")
    for yo in amigosT:
        print(yo)
mitupla()
print("")
print("Diccionario")
def midicc():
    amigosD={
        "amigo1":"Chamba",
        "amigo2":"Milic",
        "amigo3":"Robertote"
    }
    print(amigosD)
midicc()
print("")
print("Conjunto")
def miconjunto():
    amigosC={"Chamba","Milic","Robertote"}
    for yo in amigosC:
        print(yo)
miconjunto()