import sys

def main():
    # Récupérer les variables passées en argument lors de l'exécution du programme secondaire
    if len(sys.argv) < 17:
        print("Erreur : Le nombre d'arguments est insuffisant.")
        return

    nb_lines = sys.argv[1]
    iso_date = sys.argv[2]
    iso_time = sys.argv[3]
    file_format = sys.argv[4]
    file_prefix = sys.argv[5]
    output_mode = sys.argv[6]
    dest_email = sys.argv[7]
    gen_interval = sys.argv[8]
    gen_iteration = sys.argv[9]
    gen_option = sys.argv[10]
    log_option = sys.argv[11]
    ftp_host = sys.argv[12]
    ftp_port = sys.argv[13]
    ftp_username = sys.argv[14]
    ftp_password = sys.argv[15]
    filename = sys.argv[16]

    # Faire quelque chose avec les variables
    print("Variables reçues :")
    print("Nombre de lignes :", nb_lines)
    print("Adresse FTP :", ftp_host)

if __name__ == "__main__":
    main()