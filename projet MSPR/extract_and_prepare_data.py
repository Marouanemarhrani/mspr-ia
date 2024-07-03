import os
import xml.etree.ElementTree as ET
from PIL import Image

# Chemins vers les dossiers
base_dir = r'C:\Users\user\OneDrive\Documents\GitHub\mspr-ia\projet MSPR'
annotations_dir = os.path.join(base_dir, 'annotation')
images_dir = os.path.join(base_dir, 'Mammiferes')
output_dir = os.path.join(base_dir, 'output')

# Créer les dossiers de sortie si nécessaire
os.makedirs(output_dir, exist_ok=True)

# Liste des fichiers manquants
missing_files = []

# Parcourir tous les dossiers d'annotations
for animal_folder in os.listdir(annotations_dir):
    animal_path = os.path.join(annotations_dir, animal_folder)
    if os.path.isdir(animal_path):
        for annotation_file in os.listdir(animal_path):
            if annotation_file.endswith('.xml'):
                annotation_path = os.path.join(animal_path, annotation_file)
                
                # Parser le fichier XML
                tree = ET.parse(annotation_path)
                root = tree.getroot()
                
                # Obtenir le nom de fichier de l'image
                filename = root.find('filename').text
                image_path = os.path.join(images_dir, animal_folder, filename)
                
                if os.path.exists(image_path):
                    # Charger l'image
                    image = Image.open(image_path)
                    
                    # Parcourir les objets annotés dans l'image
                    for obj in root.findall('object'):
                        # Obtenir le nom de l'animal
                        animal_name = obj.find('name').text
                        
                        # Obtenir les coordonnées de la boîte englobante
                        bndbox = obj.find('bndbox')
                        xmin = int(bndbox.find('xmin').text)
                        ymin = int(bndbox.find('ymin').text)
                        xmax = int(bndbox.find('xmax').text)
                        ymax = int(bndbox.find('ymax').text)
                        
                        # Extraire la région d'intérêt (ROI)
                        roi = image.crop((xmin, ymin, xmax, ymax))
                        
                        # Chemin de sauvegarde pour l'extrait
                        animal_output_dir = os.path.join(output_dir, animal_name)
                        os.makedirs(animal_output_dir, exist_ok=True)
                        output_path = os.path.join(animal_output_dir, filename)
                        
                        # Sauvegarder l'extrait
                        roi.save(output_path)
                else:
                    missing_files.append(image_path)

print('Extraction des empreintes terminée.')
if missing_files:
    print('Les fichiers suivants sont manquants :')
    for file in missing_files:
        print(file)
