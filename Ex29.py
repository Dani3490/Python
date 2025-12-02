def comptar_majuscules(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

print("Proves")
exemples = [
    "Hola Món",
    "HELLO WORLD",
    "python programming",
    "El 2024 És Un ANY Genial!",
    "ABC123def456GHI",
    "",
    "123456",
    "àÀèÈéÉíÍóÓúÚ",
    "La CiÈnCiA és FASCINANT"
]

for exemple in exemples:
    resultat = comptar_majuscules(exemple)
    print(f"Cadena: '{exemple}'")
    print(f"Majúscules: {resultat}\n")

print("Proves")
proves_detallades = [
    "Barcelona és La Capital De Catalunya",
    "UNESCO",
    "iPhone 15 Pro Max"
]

for prova in proves_detallades:
    resultat = comptar_majuscules(prova)
    print(f"Cadena: '{prova}'")
    print(f"Total majúscules: {resultat['total']}")
    print(f"Lletres majúscules: {resultat['lletres']}")
    print(f"Percentatge: {resultat['percentatge']}%\n")

print("\n=== VERIFICACIÓ ===")
text_prova = "Python És Un Llenguatge GENIAL!"
print(f"Text: '{text_prova}'")
print(f"Versió 1: {comptar_majuscules(text_prova)}")
print(f"Versió 2: {comptar_majuscules_v2(text_prova)}")