# Initialisation des compteurs
error_count = warning_count = info_count = 0

# Lecture du fichier log.txt
try:
    with open('log.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if 'ERROR' in line:
                print(line)
                error_count += 1
            elif 'WARNING' in line:
                print(line)
                warning_count += 1
            elif 'INFO' in line:
                print(line)
                info_count += 1
except FileNotFoundError:
    print("Erreur : fichier log.txt non trouvé.")
    exit(1)

# Génération du rapport
with open('rapport.txt', 'w') as report:
    report.write(f"ERROR: {error_count}, WARNING: {warning_count}, INFO: {info_count}\n")
    print(f"Rapport généré : ERROR: {error_count}, WARNING: {warning_count}, INFO: {info_count}")

# Test simple
assert error_count >= 0, "Le nombre d'erreurs ne peut pas être négatif ?"
