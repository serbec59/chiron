import sys

def main():
    # Récupérer les variables passées en argument lors de l'exécution du programme secondaire
    if len(sys.argv) < 3:
        print("Erreur : Le nombre d'arguments est insuffisant.")
        return

    variable1 = sys.argv[1]
    variable2 = sys.argv[2]

    # Faire quelque chose avec les variables
    print("Variables reçues :")
    print("Variable 1 :", variable1)
    print("Variable 2 :", variable2)
    print(variable1, " + ",variable2, " = ", variable1 + variable2)

if __name__ == "__main__":
    main()