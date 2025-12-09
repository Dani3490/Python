from abc import ABC, abstractmethod

# Classe base Animal (abstracta)
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat
    
    @abstractmethod
    def xerrar(self):
        pass
    
    @abstractmethod
    def mourem(self):
        pass
    
    def quisoc(self):
        return f"Sóc un {self.especie} i tinc {self.edat} anys"


# Subclasse Cavall
class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)
    
    def xerrar(self):
        return "Hiiiii! Hiiiii!"
    
    def mourem(self):
        return "Galopo a quatre potes"


# Subclasse Dofí
class Dofi(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)
    
    def xerrar(self):
        return "Click click click!"
    
    def mourem(self):
        return "Nado amb la meva aleta caudal"


# Subclasse Abella
class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)
    
    def xerrar(self):
        return "Bzzzz bzzzz!"
    
    def mourem(self):
        return "Volo amb les meves ales"
    
    def picar(self):
        return "T'he picat! Ara moriré..."


# Subclasse Humà
class Huma(Animal):
    def __init__(self, edat, nom):
        super().__init__("Humà", edat)
        self.nom = nom
    
    def xerrar(self):
        return f"Hola! Em dic {self.nom}"
    
    def mourem(self):
        return "Camino amb dues cames"
    
    def quisoc(self):
        return f"Sóc {self.nom}, un {self.especie} de {self.edat} anys"


# Subclasse Fiet (hereda d'Humà)
class Fiet(Huma):
    def __init__(self, edat, nom, pares):
        super().__init__(edat, nom)
        self.pares = pares  # llista amb els noms dels pares
    
    def nompares(self):
        if len(self.pares) >= 2:
            return f"Els meus pares són: {self.pares[0]} i {self.pares[1]}"
        elif len(self.pares) == 1:
            return f"El meu pare/mare és: {self.pares[0]}"
        else:
            return "No tinc pares registrats"


# Subclasse Centaure (herència múltiple)
class Centaure(Cavall, Huma):
    def __init__(self, edat, nom):
        # Inicialitzem ambdues classes pare
        Cavall.__init__(self, edat)
        self.nom = nom
        self.especie = "Centaure"
    
    def xerrar(self):
        return f"Sóc {self.nom}! Meitat humà, meitat cavall!"
    
    def mourem(self):
        return "Galopo amb quatre potes i tinc braços humans"
    
    def quisoc(self):
        return f"Sóc {self.nom}, un {self.especie} de {self.edat} anys"


# Classe Xou (independent, però amb els mateixos mètodes)
class Xou:
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat
    
    def xerrar(self):
        return "Sóc del xou i faig sons estranys!"
    
    def mourem(self):
        return "Em moc d'una manera espectacular"
    
    def quisoc(self):
        return f"Sóc del xou: {self.especie}, {self.edat} anys"


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Creem una llista amb diferents animals i objectes
    llista_animals = [
        Cavall(5),
        Dofi(8),
        Abella(1),
        Huma(30, "Joan"),
        Huma(25, "Maria"),
        Fiet(10, "Pere", ["Joan", "Maria"]),
        Centaure(150, "Quiró"),
        Xou("Criatura màgica", 100)
    ]
    
    print("=" * 60)
    print("DEMOSTRACIÓ DE POLIMORFISME")
    print("=" * 60)
    
    # Bucle que crida als mètodes comuns
    for animal in llista_animals:
        print(f"\n{animal.quisoc()}")
        print(f"  Xerrar: {animal.xerrar()}")
        print(f"  Moure'm: {animal.mourem()}")
        
        # Mètodes específics
        if isinstance(animal, Abella):
            print(f"  Picar: {animal.picar()}")
        
        if isinstance(animal, Fiet):
            print(f"  Pares: {animal.nompares()}")
        
        print("-" * 60)
    
    # Demostració addicional amb l'abella
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓ MÈTODE ESPECÍFIC D'ABELLA")
    print("=" * 60)
    abella = Abella(2)
    print(abella.picar())
    
    # Demostració addicional amb Fiet
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓ MÈTODE ESPECÍFIC DE FIET")
    print("=" * 60)
    fiet = Fiet(12, "Anna", ["Pere", "Laura"])
    print(fiet.nompares())