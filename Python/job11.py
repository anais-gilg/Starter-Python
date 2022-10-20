#parcourir le contenu du fichier “domains.xml” et compter le nombre de noms de domaine.
#Télécharger le fichier pour l'avoir dans vscode

#importer minidom

from xml.dom import minidom

doc = minidom.parse('domains.xml')
# .parse sert à parcourir le fichier

elements = doc.getElementsByTagName("colum")
newList = []

for element in elements:
    if element.getAttribute("name") == "domain":
        newList.append(element.childNodes[0].data)
        #je veux juste le contenu texte de se document

print(len("newList"))