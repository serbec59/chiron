import subprocess

def collect_variables():
    variable1 = (input("Entrez le premier nombre : "))
    variable2 = (input("Entrez le second nombre : "))
    return variable1, variable2

def main():
    print("Bienvenue dans le programme principal.")
    var1, var2 = collect_variables()

    # Exécuter le programme secondaire en lui transmettant les variables en tant qu'arguments
    subprocess.run(["python", "programme_secondaire.py", var1, var2])

if __name__ == "__main__":
    main()