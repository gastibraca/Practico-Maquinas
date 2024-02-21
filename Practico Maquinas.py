import TDA_ENC
import TDA_PROF
TDA_ENC.Encargado.checkEnc()
TDA_PROF.Profesor.checkProf()

file = open("inscripciones.txt","r")
inscr = file.readlines()
ins = []
for i in inscr:
    inscripcion = []
    l = i.split(",")
    for x in l :
            x = x.replace("\n", "")
            inscripcion.append(x)
    ins.append(inscripcion)
file.close()

def menues(sol) :
    if sol == "encargado" :
        TDA_ENC.Encargado.menuEnc(ins)

    elif sol == "profesor":
        TDA_PROF.Profesor.menuProf(ins)
    try:
        seg = input("Desea realizar otra operacion? Si/No: ").lower()
        if seg == "si" :
            menues(sol)
        elif seg == "no" :
            print("Saludos")
        else :
            raise KeyError
    except KeyError:
        print("Opción invalida. Saludos.")

def ingreso(sol) :
    try :
        print(f"BIENVENIDO")
        if sol == "encargado" :
            TDA_ENC.Encargado.ingresoEnc()
        
        elif sol == "profesor" :
            TDA_PROF.Profesor.ingresoProf()
        else :
            raise KeyError
    except KeyError :
        print("INGRESE UN ROL VALIDO")
        sol = input("Ingrese su rol: ").lower()
        ingreso(sol)
    return sol

sol = input("Ingrese su rol (profesor o encargado): ").lower()
ingreso(sol)
menues(sol)
