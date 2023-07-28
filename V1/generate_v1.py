import random
import time
import os
import csv
from ftplib import FTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_random_french_phone_number():
    prefixes = ["06", "07"]
    prefix = random.choice(prefixes)
    suffix = "".join(random.choice("0123456789") for _ in range(8))
    return f"{prefix}{suffix}"

def generate_lines(num_lines):
    lines = []
    prev_caller_number = None
    prev_called_number = None

    for i in range(1, num_lines + 1):
        iso_date = int(time.time()) if random.choice([True, False]) else random.randint(1627574400, int(time.time()))
        iso_time = random.randint(0, 86400)
        caller_number = generate_random_french_phone_number()
        
        # Ensure the next caller number is different from the previous one
        while caller_number == prev_caller_number:
            caller_number = generate_random_french_phone_number()
        
        called_number = generate_random_french_phone_number()
        
        # Ensure the next called number is different from the previous one
        while called_number == prev_called_number:
            called_number = generate_random_french_phone_number()
        
        duration = random.randint(10, 600)
        lines.append([i, iso_date, iso_time, caller_number, called_number, duration])
        prev_caller_number = caller_number
        prev_called_number = called_number
    
    return lines

def save_to_csv(lines, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Numéro de ligne", "Date (ISO)", "Heure (ISO)", "Numéro d'appelant", "Numéro d'appelé", "Durée (secondes)"])
        for line in lines:
            writer.writerow(line)


def send_email(subject, body, to_address, from_address, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("E-mail envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")


def main():
    print("----- Générateur de lignes -----")
    
    # Menu de sélection des options
    print("Options:")
    print("1. Lancer automatiquement la génération de lignes")
    print("2. Choisir le nombre de lignes à générer")
    print("3. Choisir la date (aléatoire ou fixe)")
    print("4. Choisir l'heure (aléatoire ou fixe)")
    print("5. Sortie")
    
    auto_generate = False
    num_lines = 0
    iso_date = None
    iso_time = None
    email_enabled = False
    email_address = None

    while True:
        option = input("Choisissez une option : ")

        if option == "1":
            auto_generate = True
            num_iterations = int(input("Nombre d'itérations à effectuer : "))
            prefix = input("Préfixe du nom de fichier : ")
        elif option == "2":
            num_lines = int(input("Nombre de lignes à générer : "))
        elif option == "3":
            choice = input("Voulez-vous une date aléatoire ? (o/n) : ").lower()
            if choice == "o":
                iso_date = None
            elif choice == "n":
                iso_date = int(input("Entrez la date au format ISO (YYYYMMDD) : "))
        elif option == "4":
            choice = input("Voulez-vous une heure aléatoire ? (o/n) : ").lower()
            if choice == "o":
                iso_time = None
            elif choice == "n":
                iso_time = int(input("Entrez l'heure au format HHMMSS : "))
        elif option == "5":
            break
        elif option == "6":
            email_enabled = True
            email_address = input("Entrez l'adresse e-mail pour les statistiques de sortie : ")
        elif option == "7":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

    
    if auto_generate:
        print(f"Génération automatique de lignes pour {num_iterations} itérations avec préfixe {prefix}")
        for iteration in range(num_iterations):
            start_time = time.time()
            generated_lines = generate_lines(num_lines)
            end_time = time.time()

            time_taken = end_time - start_time
            lines_per_second = num_lines / time_taken

            print(f"\nItération {iteration + 1}")
            print(f"Temps de génération : {time_taken:.4f} secondes")
            print(f"Nombre de lignes générées : {num_lines}")
            print(f"Nombre de lignes générées par seconde : {lines_per_second:.2f}")

            filename = f"{prefix}_{time.strftime('%Y%m%d_%H%M%S')}.csv"
            save_to_csv(generated_lines, filename)
            print(f"Les lignes ont été enregistrées dans le fichier '{filename}'")

            if email_enabled:
                subject = f"Statistiques de sortie - Itération {iteration + 1}"
                body = f"Temps de génération : {time_taken:.4f} secondes\nNombre de lignes générées : {num_lines}\nNombre de lignes générées par seconde : {lines_per_second:.2f}"
                send_email(subject, body, email_address, from_address="votre_adresse_email", smtp_server="smtp.example.com", smtp_port=587, smtp_username="votre_nom_utilisateur_smtp", smtp_password="votre_mot_de_passe_smtp")
                print(f"Statistiques de sortie de l'itération {iteration + 1} envoyées à l'adresse {email_address}")
    else:
        if num_lines == 0:
            print("Nombre de lignes non spécifié. Sortie du programme.")
            return

        start_time = time.time()
        generated_lines = generate_lines(num_lines)
        end_time = time.time()

        time_taken = end_time - start_time
        lines_per_second = num_lines / time_taken

        print(f"\nTemps de génération : {time_taken:.4f} secondes")
        print(f"Nombre de lignes générées : {num_lines}")
        print(f"Nombre de lignes générées par seconde : {lines_per_second:.2f}")

        while True:
            print("\n----- Menu de sortie -----")
            print("1. Enregistrer dans un fichier CSV")
            print("2. Envoyer via FTP")
            print("3. Quitter")
            choice = input("Choisissez une option : ")

            if choice == "1":
                filename = input("Nom du fichier CSV de sortie : ")
                save_to_csv(generated_lines, filename)
                print(f"Les lignes ont été enregistrées dans le fichier '{filename}'")
            elif choice == "2":
                ftp_host = input("Adresse FTP : ")
                ftp_username = input("Nom d'utilisateur FTP : ")
                ftp_password = input("Mot de passe FTP : ")
                filename = input("Nom du fichier CSV de sortie : ")

                with FTP(ftp_host) as ftp:
                    ftp.login(user=ftp_username, passwd=ftp_password)
                    with open(filename, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Numéro de ligne", "Date (ISO)", "Heure (ISO)", "Numéro d'appelant", "Numéro d'appelé", "Durée (secondes)"])
                        for line in generated_lines:
                            writer.writerow(line)
                    ftp.storbinary(f"STOR {filename}", open(filename, "rb"))
                
                print(f"Les lignes ont été envoyées via FTP au serveur {ftp_host}")
            elif choice == "3":
                print("Programme terminé.")
                break
            else:
                print("Option invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()
