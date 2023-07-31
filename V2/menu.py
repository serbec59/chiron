from banner import *
import subprocess

## DEFINITION DES VARIABLES DE DEPART ##
def collect_variables():
    nb_lines = 0
    iso_date = None
    iso_time = None
    file_format = None
    file_prefix = None
    output_mode = None
    dest_email = None
    gen_interval = None
    gen_iteration = None
    gen_option = None
    log_option = None
    ftp_host = "127.0.0.1"
    ftp_port = 21
    ftp_username = "anonymous"
    ftp_password = None
    filename = None

    return (nb_lines, iso_date, iso_time, file_format, file_prefix, output_mode, dest_email, gen_interval,
            gen_iteration, gen_option, log_option, ftp_host, ftp_port, ftp_username, ftp_password, filename)


def main():
    ## MENU DE SELECTION DES OPTIONS ##
    print("1. Choisir le nombre de lignes à générer")
    print("2. Choisir la date (aléatoire ou fixe)")
    print("3. Choisir l'heure (aléatoire ou fixe)")
    print("4. Choisir le format de sortie")
    print("5. Définir le mode de sortie")
    print("6. Choisir les options de génération")
    print("7. Options de journalisation")
    print("8. Lancer la génération")
    print("9. Vérifier les variables")
    print("10. Quitter le programme")

    # Initialiser les variables en utilisant la fonction
    (nb_lines, iso_date, iso_time, file_format, file_prefix, output_mode, dest_email, gen_interval,
     gen_iteration, gen_option, log_option, ftp_host, ftp_port, ftp_username, ftp_password, filename) = collect_variables()

    while True:
        option = input("Choisissez une option : ")

        if option == "1":
            nb_lines = int(input("Nombre de lignes à générer : "))
        
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
            file_prefix = input("Définir le préfixe du fichier à utiliser : ")
            choice = input("Format de fichier à utiliser : 1. CSV  -  2. TXT ").lower()
            if choice == "1":
                file_format = ".csv"
            elif choice == "2":
                file_format = ".txt"
            print("Nouveau nom de fichier : ", file_prefix, file_format)
        
        elif option == "5":
            print("1. Fichier enregistré en local")
            print("2. Envoi par mail")
            print("3. Envoi par ftp")
            choice = input("Définir le mode d'envoi : ")
            if choice == "1":
                output_mode = 1
            elif choice == "2":
                dest_email = input("Entrer l'adresse email du destinataire : ")
                output_mode = 2
            elif choice == "3":
                ftp_host = input("Adresse FTP : ")
                ftp_port = int(input("Port FTP : "))
                ftp_username = input("Nom d'utilisateur FTP : ")
                ftp_password = input("Mot de passe FTP : ")
                filename = input("Nom du fichier de sortie : ")
                output_mode = 3
        
        elif option == "6":
            print("1. Génération par intervalle de temps")
            print("2. Génération par nombre d'itérations")
            print("3. Génération unique")
            choice = input("Options de génération : ")
            if choice == "1":
                gen_interval = int(input("Intervalle entre deux générations (en secondes) : "))
                gen_option = 1
            elif choice == "2":
                gen_iteration = int(input("Nombre d'itérations à réaliser : "))
                gen_option = 2
            elif choice == "3":
                gen_option = 3
        
        elif option == "7":
            print("1. Afficher les logs à chaque génération")
            print("2. Exporter les logs dans un fichier local")
            print("3. Exporter les logs vers FTP")
            choice = input("Options de journalisation : ")
            if choice == "1":
                log_option = 1
            elif choice == "2":
                log_option = 2
            elif choice == "3":
                log_option = 3
        
        elif option == "8":
            print("Lancement de la génération avec les paramètres donnés")
            subprocess.run(["python", "main.py", nb_lines, iso_date, iso_time, file_format, file_prefix, output_mode, dest_email, gen_interval,
     gen_iteration, gen_option, log_option, ftp_host, ftp_port, ftp_username, ftp_password, filename])


        elif option == "9":
            print("Résumé des variables enregistrées")
            print("Nombre de lignes à générer :", nb_lines)
            print("Date DANS la génération :", iso_date)
            print("Heure DANS la génération :", iso_time)
            print("Format de fichier :", file_format)
            print("Préfixe de nom de fichier :", file_prefix)
            print("Mode de sortie :", output_mode)
            print("Email du destinataire :", dest_email)
            print("Intervalle de génération (en sec) :", gen_interval)
            print("Nombre d'itérations à générer :", gen_iteration)
            print("Option de génération :", gen_option)
            print("Option de journalisation :", log_option)
            print("Adresse FTP :", ftp_host)
            print("Port FTP :", ftp_port)
            print("Username FTP :", ftp_username)
            print("Password FTP :", ftp_password)
            print("Nom de fichier sur le FTP :", filename)
        
        elif option == "10":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")


if __name__ == "__main__":
    main()
