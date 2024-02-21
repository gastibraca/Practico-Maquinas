dirprof = []
class Profesor() :

    def __init__(self):
        return

    def checkProf(self) :
        with open("profesores.txt","r") as arc :
            con = arc.readlines()
            for i in con:
                tupla = []
                linea = i.split(", ")
                for x in linea :
                    x = x.replace("\n", "")
                    tupla.append(x)
                dirprof.append(tuple(tupla))
        return
    
    def ingresoProf(self):
        n = input("Ingrese su nombre: ").upper()
        e = input("Ingrese la materia que dicta: ").upper()
        c = input("Ingrese el curso: ").upper()
        d = input("Ingrese la division: ").upper()
        cred = (n,e,c,d)
        try :
            if cred in dirprof :
                print("ACCESO CORRECTO")
            else :
                raise KeyError
        except KeyError :
            print("DATOS INVALIDOS. INTENTE NUEVAMENTE")
            self.ingresoProf()
        return
    
    def menuProf(self,ins) :
        acc = input(f"Que desea hacer?\nA)Cargar la nota de un alumno\nB)Modificar una nota\nC)Eliminar una inscripción\nD)Salir\nSelección: ").lower()
        try :
            if acc == "a" :
                self.profCargarNota(ins)
            elif acc == "b":
                self.profModificarNota(ins)
            elif acc == "c" :
                self.profBorrar(ins)
            elif acc == "d":
                pass
            else :
                raise KeyError
        except KeyError :
            print("SELECCIONE UNA OPCION VALIDA")
            self.menuProf(ins)

    def profCargarNota(self,ins) :
        try:
            for i in range(len(ins)) :
                print(f"{i+1}){ins[i]}")
            ing = int(input("Seleccione la nota que desea cargar: "))
            ins[ing-1][6] = input("Ingrese la nota: ").upper()
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
            self.profCargarNota(ins)

    def profModificarNota(self,ins) :
        try:
            for i in range(len(ins)) :
                print(f"{i+1}){ins[i]}")
            ing = int(input("Seleccione la nota que desea modificar: "))
            ins[ing-1][6] = input("Ingrese el nueva nota: ").upper()
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
            self.profModificarNota(ins)

    def profBorrar(self,ins) :
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
            self.profBorrar(ins)
                
Profesor = Profesor()
