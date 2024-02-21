direnc = []
class Encargado() :

    def __init__(self):
        return

    def checkEnc(self) :
        with open("encargados.txt","r") as arc :
            con = arc.readlines()
            for i in con:
                tupla = []
                linea = i.split(", ")
                for x in linea :
                    x = x.replace("\n", "")
                    tupla.append(x)
                direnc.append(tuple(tupla))
        return
    
    def ingresoEnc(self):
        n = input("Ingrese su nombre: ").upper()
        dni = input("Ingrese su DNI: ")
        cred = (n,dni)
        try :
            if cred in direnc :
                print("ACCESO CORRECTO")
            else :
                raise KeyError
        except KeyError :
            print("DATOS INVALIDOS. INTENTE NUEVAMENTE")
            self.ingresoEnc()
        return
    
    def menuEnc(self, ins) :
        acc = input(f"Que desea hacer?\nA)Inscribir un alumno\nB)Modificar una inscipción\nC)Eliminar una inscripción\nD)Salir\nSelección: ").lower()
        try :
            if acc == "a" :
                self.encInscribir(ins)
            elif acc == "b":
                self.encModificar(ins)
            elif acc == "c" :
                self.encBorrar(ins)
            elif acc == "d" :
                pass
            else :
                raise KeyError
        except KeyError :
            print("SELECCIONE UNA OPCION VALIDA")
            self.menuEnc(ins)

    def encBorrar(self,ins) :
        try:
            for i in range(len(ins)) :
                print(f"{i+1}){ins[i]}")
            ing = int(input("Inscripción que desea eliminar: "))
            del ins[ing-1]
            with open("inscripciones.txt","w") as file :
                for i in ins :
                    entry = ""
                    for x, el in enumerate(i) :
                        if x == len(i) - 1 :
                            entry += el+"\n"
                        else :
                            entry += el+","
                    file.write(entry)
        except IndexError:
            print("OPCION NO PERTENECE A UNA INSCRIPCION EXISTENTE")
            self.encBorrar(ins)
                
    def encModificar(self,ins) :
        try:
            for i in range(len(ins)) :
                print(f"{i+1}){ins[i]}")
            ing = int(input("Inscripción que desea modificar: "))
            for i in range(len(ins[ing-1])) :
                print(f"{i+1}){ins[ing-1][i]}")
            dat = int(input("ingrese el dato que desea reemplazar: "))
            ins[ing-1][dat-1] = input("Ingrese el nuevo valor: ").upper()
            with open("inscripciones.txt","w") as file :
                for i in ins :
                    entry = ""
                    for x, el in enumerate(i) :
                        if x == len(i) - 1 :
                            entry += el+"\n"
                        else :
                            entry += el+","
                    file.write(entry)
        except IndexError:
            print("OPCION NO PERTENECE A UNA INSCRIPCION EXISTENTE")
            self.encModificar(ins)
                
    def encInscribir(self,ins) :
        f = input("Ingrese la fecha de examen: ").upper()
        na = input("Ingrese el nombre del alumno: ").upper()
        m = input("Ingrese el nombre de la materia: ").upper()
        np = input("Ingrese el nombre del profesor a cargo: ").upper()
        c = input("Ingrese el curso: ").upper()
        d = input("Ingrese la division: ").upper()
        nota = "-1"
        ing = f"{f},{na},{m},{np},{c},{d},{nota}\n"
        arc = open("inscripciones.txt","a")
        arc.write(f"{ing}")
        arc.close()
        
Encargado = Encargado()
