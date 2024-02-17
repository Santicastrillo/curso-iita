#Crear una clase alumnos que te permita agregar clases,teniendo en cuenta los parametros que almacenan la informacion del alumno y metodos que te permitan ingresar una nueva nota,asignar una falta,asignar una amonestacion,cambiar domicilio
class alumnos:
    def __init__ (self,nombre,apellido,edad,domicilio,lengua,matematica,fisica,etica,faltas,amonestaciones):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.domicilio=domicilio
        self.lengua=[]
        self.matematica=[]
        self.fisica=[]
        self.etica=[]
        self.faltas=0
        self.amonestaciones=0
    
    def agregar_edad(self,edad):
        self.edad.append(edad)
            
    def agregar_nota_lengua(self,lengua):
        self.lengua.append(lengua)
    
    def agregar_nota_matematica(self,matematica):
        self.matematica.append(matematica)
    
    def agregar_nota_fisica(self,fisica):
        self.fisica.append(fisica)
    
    def agregar_nota_etica(self,etica):
        self.etica.append(etica)
                        
    def asignar_falta(self):
        self.faltas=self.faltas+1
        
    def asignar_amonestacion(self):
        self.amonestaciones=self.amonestaciones+1
        
    def cambiar_domicilio(self,nuevo_domicilio):
        self.domicilio=nuevo_domicilio
        
clases={}

def crear_clase(iita):
    clases[iita]=[]
    
def agregar_alumnos(iita,alumnos):
    if iita in clases:
        clases[iita].append(alumnos)
        print(f"Alumno {alumnos.nombre} agregado a la clase {iita}")
    else:
        print(f"la clase {iita} no existe")
        
crear_clase("A")

alumno1=alumnos( "Pablo","Escobar",17,"Barrio el huaico",(5,7,8),(7,9,4),(6,6,7),(8,8,6),7,3)
alumno2=alumnos( "Sofia","Lopez",18,"Caseros450",(9,9,7),(6,6,7),(6,7,8),(8,8,9),6,0)
alumno3=alumnos( "Jose","Ugarte",16,"Los alamos",(4,3,5),(6,5,6),(7,6,5),(4,5,3),13,14)

agregar_alumnos("A",alumno1)
agregar_alumnos("A",alumno2)
agregar_alumnos("A",alumno3)

alumno1.agregar_nota_lengua(6)
alumno1.agregar_nota_lengua(8)

alumno1.agregar_nota_matematica(5)
alumno1.agregar_nota_fisica(8)
alumno1.agregar_nota_fisica(10)
alumno1.agregar_nota_etica(6)
alumno1.agregar_nota_etica(4)

alumno2.agregar_nota_lengua(9)
alumno2.agregar_nota_matematica(8)
alumno2.agregar_nota_fisica(6)
alumno2.agregar_nota_etica(10)

alumno3.agregar_nota_lengua(6)
alumno3.agregar_nota_lengua(8)
alumno3.agregar_nota_matematica(7)
alumno3.agregar_nota_matematica(6)
alumno3.agregar_nota_fisica(8)
alumno3.agregar_nota_etica(4)
alumno3.agregar_nota_etica(6)

alumno1.asignar_falta()
alumno1.asignar_falta()
alumno1.asignar_falta()
alumno2.asignar_falta()
alumno3.asignar_falta()
alumno3.asignar_falta()
alumno3.asignar_falta()
alumno3.asignar_falta()
alumno3.asignar_falta()

alumno1.asignar_amonestacion()
alumno1.asignar_amonestacion()
alumno3.asignar_amonestacion()
alumno3.asignar_amonestacion()
alumno3.asignar_amonestacion()

alumno2.cambiar_domicilio("Parque belgrano quinta etapa")

print(f"Alumnos en la clase A:")
for alumno in clases["A"]:
    print(f"Nombre:{alumno.nombre}")
    print(f"Apellido:{alumno.apellido}")
    print(f"Edad:{alumno.edad}")
    print(f"Domicilio:{alumno.domicilio}")
    print(f"Nuevas notas de lengua:{alumno.lengua}")
    print(f"Nuevas notas de Matematica:{alumno.matematica}")
    print(f"Nuevas notas de Fisica:{alumno.fisica}")
    print(f"Nuevas notas de Etica:{alumno.etica}")
    print(f"Faltas recientes:{alumno.faltas}")
    print(f"Amonestaciones recientes:{alumno.amonestaciones}")
    
    #Castrillo Santiago
