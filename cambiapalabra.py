original = "yesos"
nueva = "tizas"


nombreF = "fichero.txt"

# Programa que me cambie las palabras. Tizas a yesos
# Instrucciones para manejo de ficheros de texto, abierto en este caso en lectura. 
# nombre es nuestra variable > ficherto.txt, donde tendremos otras dos variables; 
# original y nueva (tizas, yesos)

f = open(nombreF, "r")

texto_original = f.read()
f.close()

#replace string text.replace("tizas", "yesos")
 
texto_sustituido = texto_original.replace(original, nueva)


f = open(nombreF, "w")

f.write(texto_sustituido)
f.close()


