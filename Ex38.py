import random

def generar_codi_secret():
    """Genera un codi secret de 4 xifres aleatòries (0-9)"""
    return [random.randint(0, 9) for _ in range(4)]

def validar_entrada(entrada):
    """Valida que l'entrada sigui un número de 4 xifres"""
    if len(entrada) != 4:
        return False
    if not entrada.isdigit():
        return False
    return True

def comprovar_intent(codi_secret, intent):
    encerts = 0
    coincidencies = 0
    
    # Crear còpies per no modificar els originals
    codi_temp = codi_secret.copy()
    intent_temp = intent.copy()
    
    # Primer, comptar els encerts (posició correcta)
    for i in range(4):
        if intent_temp[i] == codi_temp[i]:
            encerts += 1
            # Marcar com a usats amb un valor impossible (-1)
            codi_temp[i] = -1
            intent_temp[i] = -2
    
    # Després, comptar les coincidències (número correcte, posició incorrecta)
    for i in range(4):
        if intent_temp[i] != -2:  # Si no s'ha comptat ja com a encert
            if intent_temp[i] in codi_temp:
                coincidencies += 1
                # Eliminar el primer que coincideixi
                index = codi_temp.index(intent_temp[i])
                codi_temp[index] = -1
    
    return encerts, coincidencies

def jugar():
    """Funció principal del joc"""
    print("=" * 50)
    print("  BENVINGUT AL MASTERMIND!")
    print("=" * 50)
    print("\nHe generat un codi secret de 4 xifres (0-9).")
    print("Intenta endevinar-lo!")
    print("\nEn cada intent et diré:")
    print("  - ENCERTS: números en la posició correcta")
    print("  - COINCIDÈNCIES: números correctes però mal posicionats")
    print("=" * 50)
    
    codi_secret = generar_codi_secret()
    intents = 0
    max_intents = 10
    
    while intents < max_intents:
        print(f"\nIntent {intents + 1}/{max_intents}")
        entrada = input("Introdueix un codi de 4 xifres: ")
        
        # Validar l'entrada
        if not validar_entrada(entrada):
            print("❌ Error! Has d'introduir exactament 4 xifres (0-9).")
            continue
        
        # Convertir l'entrada a llista d'enters
        intent = [int(x) for x in entrada]
        intents += 1
        
        # Comprovar l'intent
        encerts, coincidencies = comprovar_intent(codi_secret, intent)
        
        # Mostrar resultats
        if encerts == 4:
            print("\n" + "=" * 50)
            print("🎉 FELICITATS! Has endevinat el codi! 🎉")
            print(f"El codi era: {''.join(map(str, codi_secret))}")
            print(f"Ho has aconseguit en {intents} intents!")
            print("=" * 50)
            return
        else:
            print(f"✓ Encerts: {encerts}")
            print(f"○ Coincidències: {coincidencies}")
            print(f"  Intents restants: {max_intents - intents}")
    
    # Si s'acaben els intents
    print("\n" + "=" * 50)
    print("😢 Has esgotat tots els intents!")
    print(f"El codi secret era: {''.join(map(str, codi_secret))}")
    print("=" * 50)

def main():
    while True:
        jugar()
        
        resposta = input("\nVols jugar una altra partida? (s/n): ").lower()
        if resposta != 's':
            print("\nGràcies per jugar! Adéu! 👋")
            break

if __name__ == "__main__":
    main()