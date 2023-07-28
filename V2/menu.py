import subprocess

def collect_variables():
    variable1 = input("Entrez la première variable : ")
    variable2 = input("Entrez la deuxième variable : ")
    return variable1, variable2

def main():
    print("===GENERATEUR DE LIGNES===")
    print("1. Choisir le nombre de lignes à générer")
    print("2. Choisir la date (aléatoire ou fixe)")
    print("3. Choisir l'heure (aléatoire ou fixe)")
    print("4. Choisir le format de sortie")
    print("5. Définir le mode de sortie")
    print("5. choisir les options de génération")
    print("6. Options supplementaires")
    print("7. Lancer la génération")
    var1, var2 = collect_variables()


while True:
        option = input("Choisissez une option : ")

        if option == "1":
            num_lines = int(input("Nombre de lignes à générer : "))
        
        elif option == "2":
            choice = input("Voulez-vous une date aléatoire ? (o/n) : ").lower()
            if choice == "o":
                iso_date = None
            elif choice == "n":
                iso_date = int(input("Entrez la date au format ISO (YYYYMMDD) : "))
        
        elif option == "3":
            choice = input("Voulez-vous une heure aléatoire ? (o/n) : ").lower()
            if choice == "o":
                iso_time = None
            elif choice == "n":
                iso_time = int(input("Entrez l'heure au format HHMMSS : "))
        
        elif option == "4":
            choice == input("Format de fichier à utiliser : 1. CSV  -  2. TXT").lower()
            if choice == "1":
                file_format = ".csv"
            elif choice == "2":
                file_format == ".txt"
            file_prefix == input("Définir le préfixe du fichier à utiliser :")

        elif option == "5":
            choice == input("Définir le mode d'envoi")
            print("1. Fichier enregistré en local")
            print("2. Envoi par mail")
            print("3. Envoi par ftp")
            if choice == "1":
                output_mode == 1
            elif choice == "2":
                input("Entrer l'adresse email du destinataire")
                output_mode == 2
            elif choice == "3":
                output_mode == 3

        
        
        
        if option == "2":
            auto_generate = True
            num_iterations = int(input("Nombre d'itérations à effectuer : "))
            prefix = input("Préfixe du nom de fichier : ")
        
        elif option == "3":
            choice = input("Voulez-vous une date aléatoire ? (o/n) : ").lower()
            if choice == "o":
                iso_date = None
            elif choice == "n":
                iso_date = int(input("Entrez la date au format ISO (YYYYMMDD) : "))
        
        elif option == "5":
            break
        elif option == "6":
            email_enabled = True
            email_address = input("Entrez l'adresse e-mail pour les statistiques de sortie : ")
        elif option == "7":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

    





    # Exécuter le programme secondaire en lui transmettant les variables en tant qu'arguments
    subprocess.run(["python", "programme_secondaire.py", var1, var2])

if __name__ == "__main__":
    main()