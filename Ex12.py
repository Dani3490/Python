def majoredat(a):
     if a<18:
          print("Eres menor de edad, no puedes acceder")
     elif a>18:  
          print("Eres mayor de edad, puedes acceder")     
     else: 
          print("Tienes justo 18, vas pelao, pero puedes acceder")


a = int(input("Pon tu edad: "))
majoredat (a)
a = int(input("Pon de nuevo tu edad: "))
majoredat (a)


