import xml.etree.cElementTree as et

root= et.Element("Datos")

se= et.SubElement(root,"Redes")
et.SubElement(se,  "Nombre").text ="Catalina elizabeth santana pinales"
et.SubElement(se,  "matricula").text ="18040097"


se = et.SubElement(root,"Redes")
et.SubElement(se,  "Nombre").text ="Bernardo sifuentes"
et.SubElement(se,  "matricula").text ="18040088"

se =et.SubElement(root,"Redes")
et.SubElement(se,  "Nombre").text ="Xochitl ovalle"
et.SubElement(se,  "matricula").text ="18040026"

se = et.SubElement(root,"Redes")
et.SubElement(se,  "Nombre").text ="Andrea Rojas"
et.SubElement(se,  "matricula").text ="18040034"

se =et.SubElement(root,"Redes")
et.SubElement(se,  "Nombre").text ="Jonathan herrnandez"
et.SubElement(se,  "matricula").text ="18040077"



#alumnos de sistemas


se= et.SubElement(root,"Sistemas")
et.SubElement(se,  "Nombre").text ="eduardo Sanchez"
et.SubElement(se,  "matricula").text ="18040066"


se= et.SubElement(root,"Sistemas")
et.SubElement(se,  "Nombre").text ="Miguel Martinez "
et.SubElement(se,  "matricula").text ="18040045"

se= et.SubElement(root,"Sistemas")
et.SubElement(se,  "Nombre").text ="Ximena Ortiz"
et.SubElement(se,  "matricula").text ="18040037"


se= et.SubElement(root,"Sistemas")
et.SubElement(se,  "Nombre").text ="Francisco Gaytan"
et.SubElement(se,  "matricula").text ="18040098"


se= et.SubElement(root,"Sistemas")
et.SubElement(se,  "Nombre").text ="Alonso Reyes"
et.SubElement(se,  "matricula").text ="18040022"




#alumnos de multimedia



se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="Carolina herrnandez"
et.SubElement(se,  "matricula").text ="18040044"


se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="Dulce urbina"
et.SubElement(se,  "matricula").text ="18040067"

se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="Guztavo ovalle"
et.SubElement(se,  "matricula").text ="18040099"


se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="Josue Gonzales"
et.SubElement(se,  "matricula").text ="18040033"

se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="David Teruel"
et.SubElement(se,  "matricula").text ="18040051"


se= et.SubElement(root,"Multimedia")
et.SubElement(se,  "Nombre").text ="Raul Gonzales"
et.SubElement(se,  "matricula").text ="18040011"


tree  = et.ElementTree(root)
tree.write("Datos.xml" ,xml_declaration=True)


