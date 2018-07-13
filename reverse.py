import sys
from PIL import Image
fichero = str(sys.argv[1])
foto = Image.open(fichero)
datos = list(foto.getdata()) 
datos_invertidos = [(255 - datos[x][0], 255 - datos[x][1], 255 - datos[x][2]) for x in range(len(datos))] 
imagen_invertida = Image.new('RGB', foto.size) 
imagen_invertida.putdata(datos_invertidos) 
imagen_invertida.save('./negative/N'+fichero) 
imagen_invertida.close() 
foto.close()

 
