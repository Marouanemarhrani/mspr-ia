import os
import xml.etree.ElementTree as ET

def txt_to_xml(txt_path, xml_path):
    with open(txt_path, 'r') as txt_file:
        lines = txt_file.readlines()

    root = ET.Element('annotation')

    filename = os.path.basename(txt_path).replace('.txt', '.jpg') 
    ET.SubElement(root, 'filename').text = filename

    for line in lines:
        parts = line.strip().split()
        label = parts[0]
        xmin, ymin, width, height = map(float, parts[1:])

        obj = ET.SubElement(root, 'object')
        ET.SubElement(obj, 'name').text = label
        bbox = ET.SubElement(obj, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(int(xmin))
        ET.SubElement(bbox, 'ymin').text = str(int(ymin))
        ET.SubElement(bbox, 'xmax').text = str(int(xmin + width))
        ET.SubElement(bbox, 'ymax').text = str(int(ymin + height))

    tree = ET.ElementTree(root)
    tree.write(xml_path)

def batch_convert_txt_to_xml(txt_folder, xml_folder):
    if not os.path.exists(xml_folder):
        os.makedirs(xml_folder)

    for filename in os.listdir(txt_folder):
        if filename.endswith('.txt'):  
            txt_path = os.path.join(txt_folder, filename)
            xml_path = os.path.join(xml_folder, os.path.splitext(filename)[0] + '.xml')

            txt_to_xml(txt_path, xml_path)

txt_folder_path = "C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation_text/Ecureuil"
xml_folder_path = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation_text/Ecureuil2'
batch_convert_txt_to_xml(txt_folder_path, xml_folder_path)
