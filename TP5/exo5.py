import json

# Dictionnaire contenant les informations sur trois étudiants
etudiants = {
    "etudiants": [
        {"nom": "Alice", "âge": 20, "note": 85},
        {"nom": "Bob", "âge": 22, "note": 90},
        {"nom": "Claire", "âge": 21, "note": 88}
    ]
}

# Enregistrement des données dans un fichier JSON
try:
    with open("etudiants.json", "w", encoding="utf-8") as fichier_json:
        json.dump(etudiants, fichier_json, indent=4, ensure_ascii=False)
    print("Les informations des étudiants ont été enregistrées dans 'etudiants.json'.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")

# Lecture des données depuis le fichier JSON
try:
    with open("etudiants.json", "r", encoding="utf-8") as fichier_json:
        etudiants = json.load(fichier_json)
    
    print("Informations des étudiants :")
    for etudiant in etudiants["etudiants"]:
        print(f"Nom : {etudiant['nom']}, Âge : {etudiant['âge']}, Note : {etudiant['note']}")
except FileNotFoundError:
    print("Le fichier 'etudiants.json' n'a pas été trouvé. Assurez-vous qu'il existe.")
except json.JSONDecodeError:
    print("Le fichier JSON est invalide.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
