import os
import argparse
import chardet

def est_fichier_texte(chemin):
    try:
        with open(chemin, 'rb') as file:
            contenu = file.read(1024)  # Lire les premiers 1024 octets
        result = chardet.detect(contenu)
        if result['encoding'] is None:
            return False
        confidence = result['confidence']
        return confidence > 0.7 and not contenu.startswith(b'\x00')  # Éviter les fichiers commençant par un octet nul
    except Exception:
        return False

def lire_fichier(chemin):
    try:
        with open(chemin, 'rb') as file:
            raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        if encoding is None:
            return None
        return raw_data.decode(encoding)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {chemin}: {str(e)}")
        return None

def ecrire_contenu(fichier_sortie, nom_fichier, chemin, contenu):
    fichier_sortie.write(f"\n{'='*80}\n")
    fichier_sortie.write(f"Fichier : {nom_fichier}\n")
    fichier_sortie.write(f"Chemin : {chemin}\n")
    fichier_sortie.write(f"{'='*80}\n\n")
    fichier_sortie.write(contenu)
    fichier_sortie.write("\n\n")

def doit_ignorer_chemin(chemin):
    # Liste des dossiers à exclure
    dossiers_exclus = ['node_modules', 'dist', 'dist-electron']
    
    # Vérifier si le chemin contient un des dossiers à exclure
    for dossier in dossiers_exclus:
        if f'/{dossier}/' in chemin.replace('\\', '/') or chemin.replace('\\', '/').endswith(f'/{dossier}'):
            return True
    
    # Vérifier si c'est le fichier package-lock.json
    if os.path.basename(chemin) == 'package-lock.json':
        return True
        
    return False

def parcourir_repertoire(repertoire):
    fichiers = []
    for racine, dossiers, noms_fichiers in os.walk(repertoire):
        # Filtrer les dossiers à exclure pour éviter de les traverser
        dossiers[:] = [d for d in dossiers if d not in ['node_modules', 'dist', 'dist-electron']]
        
        for nom_fichier in noms_fichiers:
            if nom_fichier == 'package-lock.json':
                continue
                
            chemin_complet = os.path.join(racine, nom_fichier)
            if not doit_ignorer_chemin(chemin_complet) and est_fichier_texte(chemin_complet):
                fichiers.append((nom_fichier, chemin_complet))
    return fichiers

def main(repertoire):
    fichiers = parcourir_repertoire(repertoire)
    
    nom_projet = os.path.basename(repertoire)
    fichier_sortie_path = f"contenu_{nom_projet}.txt"

    with open(fichier_sortie_path, 'w', encoding='utf-8') as fichier_sortie:
        for nom_fichier, chemin in fichiers:
            contenu = lire_fichier(chemin)
            if contenu is not None:
                ecrire_contenu(fichier_sortie, nom_fichier, chemin, contenu)

    print(f"Le contenu de tous les fichiers texte a été consolidé dans '{fichier_sortie_path}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolide le contenu des fichiers texte d'un répertoire.")
    parser.add_argument("repertoire", help="Chemin du répertoire à analyser")
    args = parser.parse_args()

    main(args.repertoire)
